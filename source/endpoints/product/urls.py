"""Urls module."""

from rest_framework.routers import DefaultRouter

from source.endpoints.product.views import ProductViewSet

router = DefaultRouter()
router.register(r"", ProductViewSet, basename="publish")

urlpatterns = router.urls
