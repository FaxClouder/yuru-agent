from uuid import UUID

from fastapi import APIRouter, status

from yuru_agent_api.schemas.common import ApiResponse, ReservedCapability
from yuru_agent_api.schemas.runs import AgentRunCreate

router = APIRouter()


@router.post(
    "/agents/{agent_id}/runs",
    response_model=ApiResponse[ReservedCapability],
    status_code=status.HTTP_202_ACCEPTED,
)
def create_agent_run(agent_id: UUID, payload: AgentRunCreate) -> ApiResponse[ReservedCapability]:
    """Reserve AgentRun creation for Phase 2 Agent Runner."""
    _ = (agent_id, payload)
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 2 Agent Runner"),
        error=None,
    )


@router.get("/runs/{run_id}", response_model=ApiResponse[ReservedCapability])
def get_run(run_id: UUID) -> ApiResponse[ReservedCapability]:
    """Reserve AgentRun detail retrieval for Phase 2 Agent Runner."""
    _ = run_id
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 2 Agent Runner"),
        error=None,
    )


@router.get("/runs/{run_id}/events", response_model=ApiResponse[ReservedCapability])
def get_run_events(run_id: UUID) -> ApiResponse[ReservedCapability]:
    """Reserve streaming run events for Phase 2 Agent Runner."""
    _ = run_id
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 2 Agent Runner"),
        error=None,
    )
