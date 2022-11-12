"""Apps file."""

from django.apps import AppConfig


class AccountConfig(AppConfig):
    """Class AccountConfig."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "source.endpoints.account"
