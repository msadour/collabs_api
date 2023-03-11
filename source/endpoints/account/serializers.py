from rest_framework import serializers

from source.endpoints.account.models import Account
from source.endpoints.account.utils import update_account


class AccountSerializer(serializers.Serializer):
    def create(self, validated_data):
        new_customer: Account = Account.objects.create_user(
            username=validated_data.get("email"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
            company_name=validated_data.get("company_name"),
            siret=validated_data.get("siret"),
            k_bis=validated_data.get("k_bis"),
            address=validated_data.get("address"),
            phone=validated_data.get("phone"),
            website=validated_data.get("website"),
            industry=validated_data.get("industry"),
            speciality=validated_data.get("speciality"),
            nb_employee=validated_data.get("nb_employee"),
            headquarter=validated_data.get("headquarter"),
            description=validated_data.get("description"),
        )
        return new_customer

    def update(self, instance, validated_data):
        update_account(data=validated_data, user=instance)
        return instance

    class Meta:
        model = Account
