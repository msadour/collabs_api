"""Views account module."""

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.product.models import Product, Category
from source.layer.common.utils import get_object_or_none


class ProductViewSet(viewsets.ViewSet):
    """Class AccountViewSet."""

    def create(self, request: Request) -> Response:
        """Create a product.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        data = request.data
        user = request.user

        category = get_object_or_none(
            model_class=Category, id_to_retrieve=data.get("category", None)
        )

        Product.objects.create(
            label=data.get("label"),
            quantity=data.get("quantity"),
            description=data.get("description"),
            proposer=user,
            category=category,
        )

        return Response(status=status.HTTP_201_CREATED)
