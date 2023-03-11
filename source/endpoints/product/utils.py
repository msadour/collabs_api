from django.db.models import QuerySet

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product, Category


def get_products(query_params: dict) -> QuerySet:
    products: QuerySet = Product.objects.filter(available=True)

    for criteria, value in query_params.items():
        if criteria == "category" and value != "all":
            products: QuerySet = (
                Category.objects.filter(label__icontains=value)
                .first()
                .product_rel.all()
            )

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

        if criteria == "industry":
            products = products.filter(industry__label=value)

    return products
