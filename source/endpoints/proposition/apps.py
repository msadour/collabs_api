"""Apps file."""

from django.apps import AppConfig


class PropositionConfig(AppConfig):
    """Class PropositionConfig."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "source.endpoints.proposition"
