from typing import Generic, TypeVar

from pydantic import BaseModel

DataT = TypeVar("DataT")


class ApiResponse(BaseModel, Generic[DataT]):
    """Stable response envelope for API clients."""

    success: bool
    data: DataT | None
    error: str | None


class ReservedCapability(BaseModel):
    """Metadata returned by routes reserved for later project phases."""

    status: str
    phase: str
