"""Utils file."""

from source.endpoints.account.models import Account


def update_account(data: dict, user: Account) -> None:
    """Perform update for an account.

    Args:
        data:
        user

    Returns:
        Response from the server with list of users.
    """
    for attr, value in data.items():
        if hasattr(user, attr):
            if attr == "password":
                user.set_password(value)
            elif attr not in [
                "last_login",
                "is_superuser",
                "id",
                "is_staff",
                "groups",
                "user_permissions",
            ]:
                setattr(user, attr, value)

    user.save()
