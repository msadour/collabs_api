from django.utils.timezone import now

from django.db import models

from source.endpoints.account.models import Account
from source.layer.common.utils import get_difference_between_now_and_date


class Category(models.Model):

    label = models.CharField(max_length=255, blank=True, unique=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.label}"


class Product(models.Model):

    label = models.CharField(max_length=255, default="")
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=now)
    description = models.TextField(blank=True)
    proposer = models.ForeignKey(Account, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    @property
    def published_since(self) -> str:
        published = get_difference_between_now_and_date(self.date)
        return f"Published since {published} ago"

    def __str__(self) -> str:
        return f"{self.label}"
