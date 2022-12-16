from rest_framework.routers import DefaultRouter

from source.endpoints.product.views import ProductViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"", ProductViewSet, basename="publish")

urlpatterns: list = router.urls
