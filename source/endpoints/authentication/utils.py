from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from source.endpoints.authentication.serializers import AuthTokenSerializer


def auth_user(request: Request, serializer: AuthTokenSerializer) -> dict:
    user = serializer.validate(attrs=request.data)
    request.user = user
    token, created = Token.objects.get_or_create(user=user)
    return {
        "token": token.key,
        "email": user.email,
        "user_id": user.id,
        "is_admin": user.is_superuser,
    }
