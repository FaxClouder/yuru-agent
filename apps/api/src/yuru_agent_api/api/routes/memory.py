from fastapi import APIRouter

from yuru_agent_api.schemas.common import ApiResponse, ReservedCapability

router = APIRouter()


@router.get("", response_model=ApiResponse[ReservedCapability])
def list_memory() -> ApiResponse[ReservedCapability]:
    """Reserve memory management APIs for Phase 4 Agent Memory."""
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 4 Agent Memory"),
        error=None,
    )
