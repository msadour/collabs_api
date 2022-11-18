"""Authentication file."""

from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    """Class AuthenticationConfig."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "source.endpoints.authentication"
