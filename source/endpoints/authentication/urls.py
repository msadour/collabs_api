from django.urls import path
from rest_framework.routers import DefaultRouter

from source.endpoints.authentication.views import CustomAuthToken, LogoutViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"logout", LogoutViewSet, basename="logout")

urlpatterns: list = router.urls

urlpatterns += [path("login/", CustomAuthToken.as_view())]
