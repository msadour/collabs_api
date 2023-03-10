from typing import Any

from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product
from source.endpoints.proposition.models import Proposition, Status
from source.endpoints.proposition.utils import close_proposition


class PropositionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        product_id: str = validated_data.get("product_id")
        product: Product = Product.objects.get(product_id)

        requestor_id: str = validated_data.get("requestor_id")
        requestor: Account = Account.objects.get(requestor_id)

        seller: str = validated_data.get("seller")

        Proposition.objects.create(
            seller=seller,
            requestor=requestor,
            product=product,
            place=validated_data.get("place"),
            date_meeting=validated_data.get("date_meeting"),
            comment=validated_data.get("comment"),
        )

    def update(self, instance, validated_data):
        action: str = validated_data.get("action")

        if action == "update_info":
            field: str = self.data.get("field")
            new_value: Any = self.data.get("new_value")
            if field in ["quantity_requested", "place", "date_meeting", "comment"]:
                setattr(instance, field, new_value)
                instance.save()

        if action == "close_proposition":
            close_proposition(proposition=instance)

        # if action == "update_product":
        #     new_product: Optional[Product] = get_object_or_none(
        #         model_class=Product, id_to_retrieve=self.data.get("new_product", None)
        #     )
        #     update_product(instance, new_product=new_product)

        if action == "update_status":
            status: str = self.data.get("status")
            instance.status = (
                Status.ACCEPTED if status == "accepted" else Status.DECLINED
            )
            instance.save()

    class Meta:
        model = Proposition
