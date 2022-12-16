from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.product.serializers import ProductSerializer
from source.endpoints.product.utils import ActionProduct, get_products


class ProductViewSet(viewsets.ViewSet):
    def create(self, request: Request) -> Response:
        if bool(request.user and request.user.is_authenticated):
            return Response(status=status.HTTP_403_FORBIDDEN)

        action: ActionProduct = ActionProduct(request=request)
        action.publish_product()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request: Request) -> Response:
        products = get_products(query_params=request.query_params)
        data: ProductSerializer = ProductSerializer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request: Request):
        action = ActionProduct(request=request)

        if not action.check_owner_product():
            return Response(status=status.HTTP_403_FORBIDDEN)

        action.update_product()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request):
        action: ActionProduct = ActionProduct(request=request)

        if not action.check_owner_product():
            return Response(status=status.HTTP_403_FORBIDDEN)

        action.delete_product()

        return Response(status=status.HTTP_204_NO_CONTENT)
