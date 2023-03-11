from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.product.models import Product
from source.endpoints.product.serializers import ProductPublishedSerializer
from source.endpoints.product.utils import get_products


class ProductsAvailableViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductPublishedSerializer

    def list(self, request: Request, *args, **kwargs) -> Response:
        products: QuerySet = get_products(query_params=request.query_params)
        data: dict = self.serializer_class(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: int = None, *args, **kwargs) -> Response:
        product: Product = Product.objects.get(id=pk)
        data: dict = self.serializer_class(product).data
        return Response(data=data, status=status.HTTP_200_OK)
