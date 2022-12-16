from rest_framework import serializers

from source.endpoints.product.models import Product


class CategorySerializer(serializers.ModelSerializer):
    """Class CategorySerializer."""

    class Meta:
        """Class Meta."""

        model = Product
        fields = ("label",)


class ProductSerializer(serializers.ModelSerializer):
    """Class ProductSerializer."""

    category = CategorySerializer(many=False)
    published_since = serializers.ReadOnlyField()

    class Meta:
        """Class Meta."""

        model = Product
        fields = "__all__"
