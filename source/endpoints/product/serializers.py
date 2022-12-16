from rest_framework import serializers

from source.endpoints.product.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = ("label",)


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)
    published_since = serializers.ReadOnlyField()

    class Meta:

        model = Product
        fields = "__all__"
