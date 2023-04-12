from django.db import models


class IPBanned(models.Model):

    ip = models.GenericIPAddressField()

    objects = models.Manager()
