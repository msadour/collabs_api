"""Models file."""

from django.utils.timezone import now

from django.db import models

from source.endpoints.account.models import Account


class Category(models.Model):
    """Class Category."""

    label = models.CharField(max_length=255, blank=True)


class Product(models.Model):
    """Class Product."""

    label = models.CharField(max_length=255, default="")
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=now)
    description = models.TextField()
    proposer = models.ForeignKey(Account, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    objects = models.Manager()
