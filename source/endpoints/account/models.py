from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager

from source.plugin.address.models import Address


class Account(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company_name = models.CharField(max_length=255)
    siret = models.CharField(max_length=255)
    k_bis = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    nb_employee = models.IntegerField(default=0)
    headquarter = models.CharField(max_length=255)
    description = models.TextField()

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]
