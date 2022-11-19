"""Utils file."""
from typing import Any

from source.endpoints.product.models import Product, Category
from source.layer.common.utils import get_object_or_none


class ActionProduct:
    """Class ActionProduct."""

    def __init__(self, request):
        self.data = request.data
        self.user = request.user

    @property
    def get_product(self) -> Any:
        """Get product from data.

        Returns:
            Product.
        """
        return get_object_or_none(
            model_class=Product, id_to_retrieve=self.data.get("id")
        )

    def check_owner_product(self) -> bool:
        """Check if current user is owner of the product.

        Returns:
            Is owner or not.
        """
        return self.get_product.proposer == self.user

    def update_product(self) -> None:
        """Update product from data sent by server."""
        product = self.get_product
        for attr, value in self.data.items():
            if attr in ["label", "quantity", "description"]:
                setattr(product, attr, value)

        product.save()

    def delete_product(self) -> None:
        """Delete product."""
        if self.get_product.proposer == self.user:
            self.get_product.delete()

    def publish_product(self) -> None:
        """Publish a product."""
        category = get_object_or_none(
            model_class=Category, id_to_retrieve=self.data.get("category", None)
        )

        Product.objects.create(
            label=self.data.get("label"),
            quantity=self.data.get("quantity"),
            description=self.data.get("description"),
            proposer=self.user,
            category=category,
        )
