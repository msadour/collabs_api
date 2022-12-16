from typing import Any, Optional

from django.contrib.auth.hashers import check_password
from django.http import QueryDict
from rest_framework import serializers

from source.endpoints.account.models import Account
from source.layer.exception import AuthenticationError


class AuthTokenSerializer(serializers.Serializer):

    username: serializers.CharField = serializers.CharField()
    password: serializers.CharField = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(
        self, email: str = None, password: str = None
    ) -> Optional[Account]:
        user: Account = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationError("Not user found with this email.")

        if not user.is_active:
            raise AuthenticationError("This account is deactivate.")

        if not check_password(password, user.password):
            raise AuthenticationError("Email/Password doesn't match.")

        return user

    def validate(self, attrs: Any) -> Account:
        if type(attrs) == QueryDict:
            attrs = attrs.dict()

        email: str = attrs.get("email")
        password: str = attrs.get("password")
        user: Optional[Account] = self.authenticate_user(email=email, password=password)

        return user
