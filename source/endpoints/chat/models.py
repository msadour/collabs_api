from django.db import models
from django.utils.timezone import now

from source.endpoints.account.models import Account


class Chat(models.Model):
    participants = models.ManyToManyField(Account, related_name="chats")
    create_at = models.DateTimeField(default=now)

    objects = models.Manager()


class Message(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=now)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")

    objects = models.Manager()
