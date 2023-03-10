from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product, Category
from source.plugin.address.models import LocationProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = ("label",)


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)
    published_since = serializers.ReadOnlyField()

    def create(self, validated_data):
        category = Category.objects.get(validated_data.get("category"))
        user = Account.objects.get(validated_data.get("user_id"))

        location = LocationProduct.objects.create(
            country=validated_data.get("country", user.address.country),
            region=validated_data.get("region", user.address.region),
            city=validated_data.get("city", user.address.city),
        )

        Product.objects.create(
            label=validated_data.get("label"),
            quantity=validated_data.get("quantity"),
            description=validated_data.get("description"),
            proposer=user,
            category=category,
            location=location,
        )

    def update(self, instance, validated_data):
        for attr, value in validated_data:
            if attr in ["label", "quantity", "description"]:
                setattr(instance, attr, value)

        instance.save()

    class Meta:

        model = Product
        fields = "__all__"
