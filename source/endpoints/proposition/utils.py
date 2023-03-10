from datetime import datetime

from django.db.models import QuerySet

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product
from source.endpoints.proposition.models import Proposition


def get_queryset_propositions(user: Account, data: dict) -> QuerySet:
    type_proposition: str = data.get("type")

    if type_proposition == "proposition_from_me":
        queryset = Proposition.objects.filter(seller=user)
    elif type_proposition == "proposition_from_seller":
        queryset = Proposition.objects.filter(proposition_from_seller=user)
    else:
        raise Exception(
            "type_proposition must be proposition_from_me or proposition_from_seller"
        )

    return queryset


def close_proposition(proposition: Proposition) -> None:
    product: Product = proposition.product
    quantity_requested: int = proposition.quantity_requested

    product.quantity -= quantity_requested

    proposition.date_closing = datetime.now()
    proposition.closed = True

    proposition.save()
    product.save()


def cancel_proposition(data: dict) -> None:
    id_proposition: str = data.get("proposition_id")
    proposition: Proposition = Proposition.objects.get(id_proposition)
    proposition.delete()
