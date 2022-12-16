"""Utils file."""

from typing import Any
from datetime import datetime, timezone

import pytz

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


def get_difference_between_now_and_date(date_to_compare: Any) -> str:
    """
    Get the difference between today and date notification.

    Args:
        date_to_compare:

    Return:
        Difference in years/months/week/days/hours/minutes/seconds
    """
    now = datetime.now(timezone.utc)
    duration = now - date_to_compare.astimezone(pytz.timezone("Europe/Berlin"))
    duration_in_second = duration.total_seconds()

    seconds_in_year = 31536000
    seconds_in_month = 2628000
    seconds_in_week = 604800
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60

    if divmod(duration_in_second, seconds_in_year)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_year)[0])}y"

    if divmod(duration_in_second, seconds_in_month)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_month)[0])}mo"

    if divmod(duration_in_second, seconds_in_week)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_week)[0])}w"

    if divmod(duration_in_second, seconds_in_day)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_day)[0])}d"

    if divmod(duration_in_second, seconds_in_hour)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_hour)[0])}h"

    if divmod(duration_in_second, seconds_in_minute)[0] > 0.0:
        return f"{int(divmod(duration_in_second, seconds_in_minute)[0])}m"

    return f"{str(int(duration_in_second))}s"


def translate_value(value: str) -> Any:
    """
    Get value as python from string.

    Args:
        value:

    Return:
        value in Python.
    """
    if type(value) == str:
        return eval(value)
    return value
