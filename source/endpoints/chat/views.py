from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.chat.models import Chat, Message
from source.endpoints.chat.serializers import (
    MessageSerializer,
    ChatsSerializer,
    ChatSerializer,
)
from source.layer.common.permissions import MessagePermission, ChatPermission


class ChatViewSet(viewsets.ViewSet):
    serializer_class = ChatsSerializer
    queryset = Chat.objects.all().order_by("create_at")
    permission_classes = (
        IsAuthenticated,
        ChatPermission,
    )

    def list(self, request, *args, **kwargs):
        my_chats = self.queryset.filter(participants__id=request.user.id)
        data = self.serializer_class(my_chats, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: str = None):
        my_chat = self.queryset.get(id=pk)
        data = ChatSerializer(my_chat).data
        return Response(data=data, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        chat_id: str = request.data.get("id")
        chat: Chat = Chat.objects.get(chat_id)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageViewSet(viewsets.ViewSet):

    serializer_class = MessageSerializer
    permission_classes = (
        IsAuthenticated,
        MessagePermission,
    )

    def create(self, request: Request):
        data = request.data.copy()
        data["user"] = request.user
        message: Message = self.serializer_class().create(validated_data=data)
        message_data = self.serializer_class(message).data
        return Response(message_data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, pk: str = None) -> Response:
        message: Message = Message.objects.get(id=pk)
        content_updated: str = request.data.get("content")
        serializer: MessageSerializer = self.serializer_class(
            instance=message, data={"content": content_updated}, partial=True
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        message_id: str = request.data.get("id")
        message: Message = Message.objects.get(message_id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
