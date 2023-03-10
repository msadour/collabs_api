from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response

from source.endpoints.account.models import Account
from source.endpoints.account.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class: AccountSerializer = AccountSerializer
    queryset: QuerySet = Account.objects.all()

    def create(self, request: Request, *args, **kwargs) -> Response:
        new_customer: Account = self.serializer_class.save(data=request.data)
        data: dict = self.serializer_class(new_customer).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def list(self, request: Request, *args, **kwargs) -> Response:
        data: list = self.serializer_class(self.queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def patch(self, request: Request):
        self.serializer_class.update(instance=request.user, validated_data=request.data)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request: Request):
        account: Account = Account.objects.get(id=request.user.id)
        account.delete()
        return Response(
            data={"message": "Account deleted"}, status=status.HTTP_204_NO_CONTENT
        )
