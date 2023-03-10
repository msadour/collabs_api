from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.account.utils import update_account


class AccountSerializer(serializers.Serializer):
    def save(self, data):
        new_customer: Account = Account.objects.create_user(
            username=data.get("email"),
            email=data.get("email"),
            password=data.get("password"),
            company_name=data.get("company_name"),
            siret=data.get("siret"),
            k_bis=data.get("k_bis"),
            address=data.get("address"),
            phone=data.get("phone"),
            website=data.get("website"),
            industry=data.get("industry"),
            speciality=data.get("speciality"),
            nb_employee=data.get("nb_employee"),
            headquarter=data.get("headquarter"),
            description=data.get("description"),
        )
        return new_customer

    def update(self, instance, validated_data):
        update_account(data=validated_data, user=instance)
        return instance

    class Meta:
        model = Account
