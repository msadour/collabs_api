"""User serializer module."""


from typing import Any

from django.contrib.auth.hashers import check_password
from django.http import QueryDict
from rest_framework import serializers

from source.endpoints.account.models import Account
from source.layer.exception import AuthenticationError


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(self, email: str = None, password: str = None) -> Any:
        """Authenticate with username and password.

        Args:
            email:
            password:

        Returns:
            User.
        """
        user = Account.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationError("Not user found with this email.")

        if not user.is_active:
            raise AuthenticationError("This account is deactivate.")

        if not check_password(password, user.password):
            raise AuthenticationError("Email/Password doesn't match.")

        return user

    def validate(self, attrs: Any) -> Account:
        """Validate a member with credentials.

        Args:
            attrs: Datas from the view.

        Returns:
            User authenticate.
        """
        if type(attrs) == QueryDict:
            attrs = attrs.dict()
        email = attrs.get("email")
        password = attrs.get("password")
        user = self.authenticate_user(email=email, password=password)
        return user
