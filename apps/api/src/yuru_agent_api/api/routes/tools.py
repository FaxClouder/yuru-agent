from fastapi import APIRouter

from yuru_agent_api.schemas.common import ApiResponse, ReservedCapability

router = APIRouter()


@router.get("", response_model=ApiResponse[ReservedCapability])
def list_tools() -> ApiResponse[ReservedCapability]:
    """Reserve tool registry APIs for Phase 7 Tool Registry."""
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 7 Tool Registry"),
        error=None,
    )
