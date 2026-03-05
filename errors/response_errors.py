class DefaultResponseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class UserNotFoundError(DefaultResponseError):
    def __init__(self):
        super().__init__("User not found")


class AuthenticationError(DefaultResponseError):
    def __init__(self):
        super().__init__("Authentication Failed")


class DuplicateUserError(DefaultResponseError):
    def __init__(self):
        super().__init__("User already exists")
