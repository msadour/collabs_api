from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from source.endpoints.product.models import Product
from source.endpoints.product.serializers import ProductSerializer
from source.endpoints.product.utils import get_products


class ProductViewSet(viewsets.ViewSet):

    serializer_class = ProductSerializer()
    permission_classes = [IsAuthenticated]

    def create(self, request: Request) -> Response:
        data: dict = request.data.copy()
        data["user_id"] = request.user.id
        self.serializer_class.create(validated_data=data)
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request: Request) -> Response:
        products: QuerySet = get_products(query_params=request.query_params)
        data: dict = ProductSerializer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request: Request):
        product_id: str = request.data.get("id")
        product: Product = Product.objects.get(product_id)
        self.serializer_class.update(instance=product, validated_data=request.data)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request):
        product_id: str = request.data.get("id")
        product: Product = Product.objects.get(product_id)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
