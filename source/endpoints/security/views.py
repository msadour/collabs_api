from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from source.endpoints.security.models import IPBanned


class IPBannedViewSet(viewsets.ModelViewSet):

    queryset: QuerySet = IPBanned.objects.all()
    permission_classes = (IsAdminUser,)
