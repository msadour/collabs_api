from typing import Optional

from django.db.models import QuerySet

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product, Category
from source.layer.common.utils import get_object_or_none
from source.plugin.address.models import LocationProduct


class ActionProduct:
    def __init__(self, request):
        self.data = request.data
        self.user = request.user

    @property
    def get_product(self) -> Optional[Product]:
        return get_object_or_none(
            model_class=Product, id_to_retrieve=self.data.get("id")
        )

    def check_owner_product(self) -> bool:
        return self.get_product.proposer == self.user

    def update_product(self) -> None:
        product: Optional[Product] = self.get_product
        for attr, value in self.data.items():
            if attr in ["label", "quantity", "description"]:
                setattr(product, attr, value)

        product.save()

    def delete_product(self) -> None:
        if self.get_product.proposer == self.user:
            self.get_product.delete()

    def publish_product(self) -> None:
        category: Optional[Category] = get_object_or_none(
            model_class=Category, id_to_retrieve=self.data.get("category", None)
        )

        location = LocationProduct.objects.create(
            country=self.data.get("country", self.user.address.country),
            region=self.data.get("region", self.user.address.region),
            city=self.data.get("city", self.user.address.city),
        )

        Product.objects.create(
            label=self.data.get("label"),
            quantity=self.data.get("quantity"),
            description=self.data.get("description"),
            proposer=self.user,
            category=category,
            location=location,
        )


def get_products(query_params: dict) -> QuerySet:
    products: QuerySet = Product.objects.filter(available=True)

    for criteria, value in query_params.items():
        if criteria == "criteria":
            if value != "all":
                category_obj: QuerySet = Category.objects.filter(
                    label__icontains=value
                ).first()
                if category_obj:
                    products = products.filter(category=category_obj)

        if criteria == "company":
            company = Account.objects.get(id=value)
            products = products.filter(proposer=company)

        if criteria == "country":
            products = products.filter(proposer__address__country=value)

        if criteria == "region":
            products = products.filter(proposer__address__region=value)

        if criteria == "city":
            products = products.filter(proposer__address__city=value)

        if criteria == "quantity":
            products = products.filter(quantity=value)

        if criteria == "label":
            products = products.filter(label__icontains=value)

    return products
