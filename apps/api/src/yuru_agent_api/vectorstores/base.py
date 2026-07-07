from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class VectorItem:
    id: str
    embedding: list[float]
    metadata: dict[str, str]


class VectorStore(ABC):
    """Provider-neutral vector store contract for Milvus or pgvector adapters."""

    @abstractmethod
    async def upsert(self, items: list[VectorItem]) -> None:
        """Insert or update vector records."""

    @abstractmethod
    async def search(self, embedding: list[float], top_k: int) -> list[VectorItem]:
        """Return nearest vector records for an embedding."""

    @abstractmethod
    async def delete(self, ids: list[str]) -> None:
        """Delete vector records by ID."""
