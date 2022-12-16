class AuthenticationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ObjectDoesNotExistError(Exception):
    """The requested object does not exist."""

    silent_variable_failure: bool = True
