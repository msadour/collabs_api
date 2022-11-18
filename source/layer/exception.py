"""Exception module."""


class AuthenticationError(Exception):
    """Class AuthenticationError."""

    def __init__(self, message):
        """Check email format.

        Args:
            message:
        """
        self.message = message
        super().__init__(self.message)


class ObjectDoesNotExistError(Exception):
    """The requested object does not exist."""

    silent_variable_failure = True
