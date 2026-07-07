from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class AgentBase(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str = ""
    system_prompt: str = ""
    model: str = "gpt-4.1-mini"
    memory_enabled: bool = False
    rag_enabled: bool = False


class AgentCreate(AgentBase):
    """Payload reserved for Phase 1 agent creation."""


class AgentUpdate(BaseModel):
    """Partial payload reserved for Phase 1 agent updates."""

    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = None
    system_prompt: str | None = None
    model: str | None = None
    memory_enabled: bool | None = None
    rag_enabled: bool | None = None


class AgentRead(AgentBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
