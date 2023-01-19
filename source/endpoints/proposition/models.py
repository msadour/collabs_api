from django.utils.timezone import now

from django.db import models

from source.endpoints.account.models import Account
from source.endpoints.product.models import Product
from source.plugin.address.models import Address


class Status(models.TextChoices):

    ACCEPTED = "accepted"
    DECLINED = "declined"


class Proposition(models.Model):

    seller = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="seller")
    requestor = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="requestor"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_requested = models.IntegerField(default=1)
    place = models.CharField(max_length=255)
    date_meeting = models.DateTimeField(default=now)
    date_closing = models.DateTimeField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    closed = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=Status.choices, null=True)
    comment = models.TextField()

    objects = models.Manager()

    class Meta:

        unique_together = ("seller", "requestor", "product")
