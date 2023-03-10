from django.db import models

from source.endpoints.account.models import Account


class Chat(models.Model):
    participants = models.ManyToManyField(Account)
    create_at = models.DateTimeField()


class Message(models.Model):
    content = models.TextField()
    authors = models.OneToOneField(Account, on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
