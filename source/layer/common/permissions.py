from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from source.endpoints.product.models import Product
from source.endpoints.proposition.models import Proposition


class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "GET"


class ManagementPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: ViewSet):
        if view.action == "post":
            return request.user is not None

    def has_object_permission(
        self, request: Request, view: ViewSet, obj: Product
    ) -> bool:
        return (
            request.user == obj.proposer if view.action in ["put", "patch"] else False
        )


class UpdateOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: ViewSet, obj: Any) -> bool:
        if view.action in ["put", "patch"]:
            if type(obj) == Product:
                return request.user == obj.proposer
            elif type(obj) == Proposition:
                return request.user == obj.seller

        return False
