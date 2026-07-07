from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from yuru_agent_api.schemas.common import ApiResponse


def register_error_handlers(app: FastAPI) -> None:
    """Register a stable fallback error shape for unexpected exceptions."""

    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
        _ = request
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=ApiResponse(success=False, data=None, error=str(exc)).model_dump(),
        )
