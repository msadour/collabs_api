from django.http import JsonResponse
from rest_framework.request import Request

from source.endpoints.account.models import IPBanned


class CheckIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def ip_banned(self, request: Request) -> bool:
        x_forwarded_for: str = request.META.get("HTTP_X_FORWARDED_FOR")
        ip: str = (
            x_forwarded_for.split(",")[0]
            if x_forwarded_for
            else request.META.get("REMOTE_ADDR")
        )
        return IPBanned.objects.filter(ip=ip).first() is not None

    def __call__(self, request: Request) -> JsonResponse:
        if self.ip_banned(request=request):
            return JsonResponse({"error": "Your IP is banned."}, status=403)

        return self.get_response(request)
