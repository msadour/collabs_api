"""Urls module."""

from rest_framework.routers import DefaultRouter

from source.endpoints.account.views import AccountViewSet

router = DefaultRouter()
router.register(r"", AccountViewSet, basename="logout")

urlpatterns = router.urls
