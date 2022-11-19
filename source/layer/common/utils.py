"""Utils file."""

from typing import Any

from django.core.exceptions import ObjectDoesNotExist


def get_object_or_none(model_class: Any, id_to_retrieve: Any) -> Any:
    """Retrieve an object or return none.

    Args:
        model_class: Model class of django db.
        id_to_retrieve:

    Returns:
        Object or none.
    """
    if id_to_retrieve is None:
        return None

    try:
        object_from_db = model_class.objects.get(id=id_to_retrieve)
    except ObjectDoesNotExist:
        object_from_db = None

    return object_from_db
