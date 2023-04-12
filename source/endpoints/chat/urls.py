from rest_framework.routers import DefaultRouter

from source.endpoints.chat.views import ChatViewSet, MessageViewSet

router: DefaultRouter = DefaultRouter()
router.register(r"chat", ChatViewSet, basename="chat")
router.register(r"message", MessageViewSet, basename="message")

urlpatterns: list = router.urls
