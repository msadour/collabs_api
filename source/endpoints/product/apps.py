"""Apps file."""

from django.apps import AppConfig


class ProductConfig(AppConfig):
    """Class ProductConfig."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "source.endpoints.product"
