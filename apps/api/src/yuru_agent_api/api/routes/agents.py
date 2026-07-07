from uuid import UUID

from fastapi import APIRouter, status

from yuru_agent_api.schemas.agents import AgentCreate, AgentRead, AgentUpdate
from yuru_agent_api.schemas.common import ApiResponse, ReservedCapability

router = APIRouter()


@router.get("", response_model=ApiResponse[list[AgentRead]])
def list_agents() -> ApiResponse[list[AgentRead]]:
    """Reserved for Phase 1 Agent Workspace."""
    return ApiResponse(success=True, data=[], error=None)


@router.post(
    "",
    response_model=ApiResponse[ReservedCapability],
    status_code=status.HTTP_202_ACCEPTED,
)
def create_agent(payload: AgentCreate) -> ApiResponse[ReservedCapability]:
    """Reserve the create-agent contract without implementing persistence yet."""
    _ = payload
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 1 Agent Workspace"),
        error=None,
    )


@router.get("/{agent_id}", response_model=ApiResponse[ReservedCapability])
def get_agent(agent_id: UUID) -> ApiResponse[ReservedCapability]:
    """Reserve the agent detail contract for the workspace phase."""
    _ = agent_id
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 1 Agent Workspace"),
        error=None,
    )


@router.patch("/{agent_id}", response_model=ApiResponse[ReservedCapability])
def update_agent(agent_id: UUID, payload: AgentUpdate) -> ApiResponse[ReservedCapability]:
    """Reserve the agent update contract for the workspace phase."""
    _ = (agent_id, payload)
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 1 Agent Workspace"),
        error=None,
    )


@router.delete("/{agent_id}", response_model=ApiResponse[ReservedCapability])
def delete_agent(agent_id: UUID) -> ApiResponse[ReservedCapability]:
    """Reserve the agent delete contract for the workspace phase."""
    _ = agent_id
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 1 Agent Workspace"),
        error=None,
    )
