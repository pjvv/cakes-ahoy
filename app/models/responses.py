from models.base_models import CamelModel


class BadRequestResponse(CamelModel):
    """Response model for HTTP status code 400."""

    response_code: str = "BAD_REQUEST"
    response_message: str = "Invalid request."


class InternalErrorResponse(CamelModel):
    """Response model for HTTP status code 500."""

    response_code: str = "INTERNAL_ERROR"
    response_message: str | None = None
