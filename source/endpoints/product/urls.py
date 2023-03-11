from rest_framework.routers import DefaultRouter

from source.endpoints.product.views.product_managment import ProductViewSet
from source.endpoints.product.views.products_available import ProductsAvailableViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"manage", ProductViewSet, basename="publish")
router.register(r"all", ProductsAvailableViewSet, basename="all")

urlpatterns: list = router.urls
