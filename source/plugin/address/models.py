from django.db import models


class Location(models.Model):
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        abstract = True


class Address(Location):

    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    additional_information = models.CharField(max_length=255, null=True, blank=True)


class LocationProduct(Location):
    pass


class LocationProposition(Location):
    pass
