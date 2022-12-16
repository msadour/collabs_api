from rest_framework.routers import DefaultRouter

from source.endpoints.proposition.views import PropositionViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"", PropositionViewSet, basename="")

urlpatterns: list = router.urls
