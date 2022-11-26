"""Urls module."""

from rest_framework.routers import DefaultRouter

from source.endpoints.proposition.views import PropositionViewSet

router = DefaultRouter()
router.register(r"", PropositionViewSet, basename="")

urlpatterns = router.urls
