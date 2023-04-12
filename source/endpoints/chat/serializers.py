from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.chat.models import Chat, Message
from source.endpoints.chat.utils import create_or_get_chat


class MessageSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict):
        author: Account = validated_data["user"]
        receiver_id: str = validated_data.get("id_receiver")
        receiver: Account = Account.objects.get(id=receiver_id)

        if receiver is None:
            raise Exception("A message must be have a receiver")

        if author == receiver:
            raise Exception("Author and receiver must be different")

        chat: Chat = create_or_get_chat(author=author, receiver=receiver)

        content: str = validated_data.get("content")
        message: Message = Message.objects.create(
            content=content, author=author, chat=chat
        )

        return message

    def update(self, instance: Message, validated_data: dict):
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance

    class Meta:
        model = Message
        fields = "__all__"


class AccountMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "company_name")


class MessageInChatSerializer(serializers.ModelSerializer):

    author = AccountMessageSerializer()

    class Meta:
        model = Message
        fields = ("id", "content", "author")


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):

    messages = MessageInChatSerializer(many=True)

    class Meta:
        model = Chat
        fields = ("id", "messages", "participants")
