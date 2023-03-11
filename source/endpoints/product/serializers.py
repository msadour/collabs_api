from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product, Category
from source.plugin.address.models import LocationProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = "__all__"


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

    def update(self, instance: Product, validated_data: dict):
        for attr, value in validated_data.items():
            if attr in ["label", "quantity", "description"]:
                setattr(instance, attr, value)
            if attr == "category":
                new_category: Category = Category.objects.get(id=value)
                instance.category = new_category

        instance.save()

    class Meta:

        model = Product
        fields = "__all__"


class ProductPublishedSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)
    published_since = serializers.ReadOnlyField()

    class Meta:

        model = Product
        exclude = ("id", "date")
