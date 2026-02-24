class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class NotFoundException(AppException):
    def __init__(self, resource: str, identifier: str | int) -> None:
        super().__init__(
            message=f"{resource} '{identifier}' not found.",
            status_code=404,
        )


class ConflictException(AppException):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, status_code=409)


class UnprocessableEntityException(AppException):
    def __init__(self, message: str) -> None:
        super().__init__(message=message, status_code=422)


class ExternalServiceException(AppException):
    def __init__(self, service: str, detail: str) -> None:
        super().__init__(
            message=f"External service '{service}' error: {detail}",
            status_code=502,
        )
