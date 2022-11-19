"""Views account module."""

from django.forms.models import model_to_dict

from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.product.models import Product
from source.endpoints.product.utils import ActionProduct


class ProductViewSet(viewsets.ViewSet):
    """Class ProductViewSet."""

    def create(self, request: Request) -> Response:
        """Create a product.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        if bool(request.user and request.user.is_authenticated):
            return Response(status=status.HTTP_403_FORBIDDEN)

        action = ActionProduct(request=request)
        action.publish_product()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request: Request) -> Response:
        """List all product.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server with list of users.
        """
        data: list = [
            model_to_dict(product) for product in Product.objects.filter(available=True)
        ]
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request: Request):
        """Update a product.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        action = ActionProduct(request=request)

        if not action.check_owner_product():
            return Response(status=status.HTTP_403_FORBIDDEN)

        action.update_product()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request):
        """Delete a product.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server.
        """
        action = ActionProduct(request=request)

        if not action.check_owner_product():
            return Response(status=status.HTTP_403_FORBIDDEN)

        action.delete_product()

        return Response(status=status.HTTP_204_NO_CONTENT)
