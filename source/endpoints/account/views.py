"""Views account module."""

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.forms.models import model_to_dict

from source.endpoints.account.models import Account


class AccountViewSet(viewsets.ViewSet):
    """Class AccountViewSet."""

    def create(self, request: Request) -> Response:
        """Create a user.

        Args:
            request: request sent by the client.


        Returns:
            Response from the server.
        """
        data: dict = request.data
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
        response_data: dict = model_to_dict(new_customer)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request: Request) -> Response:
        """List all account.

        Args:
            request: request sent by the client.

        Returns:
            Response from the server with list of users.
        """
        data: list = [model_to_dict(account) for account in Account.objects.all()]
        return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, pk: int = None):
        """Delete an account.

        Args:
            request: request sent by the client.
            pk: id of account

        Returns:
            Response from the server.
        """
        try:
            account: Account = Account.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
