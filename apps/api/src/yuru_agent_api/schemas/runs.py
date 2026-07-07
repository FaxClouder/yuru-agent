from pydantic import BaseModel, Field


class AgentRunCreate(BaseModel):
    """Payload reserved for Phase 2 run creation."""

    user_task: str = Field(min_length=1)
