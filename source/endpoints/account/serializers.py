from rest_framework import serializers

from source.endpoints.account.models import Account, Industry
from source.plugin.address.models import Address


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        address = Address.objects.get(id=1)
        industry = Industry.objects.get(id=1)
        new_customer: Account = Account.objects.create_user(
            username=validated_data.get("email"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
            company_name=validated_data.get("company_name"),
            siret=validated_data.get("siret"),
            k_bis=validated_data.get("k_bis"),
            address=address,
            phone=validated_data.get("phone"),
            website=validated_data.get("website"),
            industry=industry,
            speciality=validated_data.get("speciality"),
            nb_employee=validated_data.get("nb_employee"),
            headquarter=validated_data.get("headquarter"),
            description=validated_data.get("description"),
        )
        return new_customer

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if hasattr(instance, attr):
                if attr == "password":
                    instance.set_password(value)
                elif attr not in [
                    "last_login",
                    "is_superuser",
                    "id",
                    "is_staff",
                    "groups",
                    "user_permissions",
                ]:
                    setattr(instance, attr, value)

        instance.save()

    class Meta:
        model = Account
        fields = "__all__"
