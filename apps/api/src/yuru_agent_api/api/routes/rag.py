from fastapi import APIRouter

from yuru_agent_api.schemas.common import ApiResponse, ReservedCapability

router = APIRouter()


@router.get("", response_model=ApiResponse[ReservedCapability])
def list_knowledge_bases() -> ApiResponse[ReservedCapability]:
    """Reserve knowledge base APIs for Phase 5 Knowledge Base and RAG."""
    return ApiResponse(
        success=True,
        data=ReservedCapability(status="reserved", phase="Phase 5 Knowledge Base and RAG"),
        error=None,
    )
