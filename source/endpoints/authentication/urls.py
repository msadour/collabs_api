"""Urls module."""


from django.urls import path
from rest_framework.routers import DefaultRouter

from source.endpoints.authentication.views import CustomAuthToken, LogoutViewSet

router = DefaultRouter()
router.register(r"logout", LogoutViewSet, basename="logout")

urlpatterns = router.urls

urlpatterns += [path("login/", CustomAuthToken.as_view())]
