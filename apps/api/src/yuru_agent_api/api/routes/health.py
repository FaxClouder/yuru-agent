from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from yuru_agent_api.core.database import check_database
from yuru_agent_api.schemas.common import ApiResponse

router = APIRouter()


@router.get("/db", response_model=ApiResponse[dict[str, str]])
def database_health() -> ApiResponse[dict[str, str]] | JSONResponse:
    """Check whether the configured relational database accepts a simple query."""
    result = check_database()
    if result.ok:
        return ApiResponse(success=True, data={"status": "ok"}, error=None)

    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content=ApiResponse(
            success=False,
            data={"status": "unavailable"},
            error=result.error,
        ).model_dump(),
    )
