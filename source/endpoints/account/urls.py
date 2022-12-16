from rest_framework.routers import DefaultRouter

from source.endpoints.account.views import AccountViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"", AccountViewSet, basename="logout")

urlpatterns: list = router.urls
