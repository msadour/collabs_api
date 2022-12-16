from datetime import datetime
from typing import Any, Optional

from django.forms.models import model_to_dict

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product
from source.endpoints.proposition.models import Proposition, Status
from source.layer.common.utils import get_object_or_none


class ActionProposition:
    def __init__(self, request):
        self.data = request.data
        self.user = request.user

    def make_proposition(self) -> None:
        product: Optional[Product] = get_object_or_none(
            model_class=Product, id_to_retrieve=self.data.get("product", None)
        )
        requestor: Optional[Account] = get_object_or_none(
            model_class=Account, id_to_retrieve=self.data.get("requestor", None)
        )

        Proposition.objects.create(
            seller=self.user,
            requestor=requestor,
            product=product,
            place=self.data.get("place"),
            date_meeting=self.data.get("date_meeting"),
            comment=self.data.get("comment"),
        )

    def retrieve_proposition(self) -> list:
        type_proposition: str = self.data.get("type")

        if type_proposition == "proposition_from_me":
            return [
                model_to_dict(proposition)
                for proposition in Proposition.objects.filter(seller=self.user)
            ]
        elif type_proposition == "proposition_from_seller":
            return [
                model_to_dict(proposition)
                for proposition in Proposition.objects.filter(requestor=self.user)
            ]

        return []

    @staticmethod
    def close_proposition(proposition: Proposition) -> None:
        product: Product = proposition.product
        quantity_requested: int = proposition.quantity_requested

        product.quantity -= quantity_requested

        proposition.date_closing = datetime.now()
        proposition.closed = True

        proposition.save()
        product.save()

    @staticmethod
    def update_product(proposition: Proposition, new_product: Product) -> None:
        proposition.product = new_product
        proposition.save()

    @staticmethod
    def update_info(proposition: Proposition, field: str, new_value: Any) -> None:
        if field in ["quantity_requested", "place", "date_meeting", "comment"]:
            setattr(proposition, field, new_value)
            proposition.save()

    @staticmethod
    def update_status(proposition: Proposition, status: str) -> None:
        proposition.status = (
            Status.ACCEPTED if status == "accepted" else Status.DECLINED
        )
        proposition.save()

    def update_proposition(self) -> None:
        proposition: Optional[Proposition] = get_object_or_none(
            model_class=Proposition, id_to_retrieve=self.data.get("proposition", None)
        )
        action: str = self.data.get("action")

        if action == "update_info":
            field: str = self.data.get("field")
            new_value: Any = self.data.get("new_value")
            self.update_info(proposition=proposition, field=field, new_value=new_value)

        if action == "close_proposition":
            self.close_proposition(proposition=proposition)

        if action == "update_product":
            new_product: Optional[Product] = get_object_or_none(
                model_class=Product, id_to_retrieve=self.data.get("new_product", None)
            )
            self.update_product(proposition, new_product=new_product)

        if action == "update_status":
            status: str = self.data.get("status")
            self.update_status(proposition=proposition, status=status)
