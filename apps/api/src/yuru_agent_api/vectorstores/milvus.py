from yuru_agent_api.vectorstores.base import VectorItem, VectorStore


class MilvusVectorStore(VectorStore):
    """Milvus adapter placeholder reserved for Memory and RAG phases."""

    async def upsert(self, items: list[VectorItem]) -> None:
        _ = items
        raise NotImplementedError("Milvus writes are reserved for Memory and RAG phases.")

    async def search(self, embedding: list[float], top_k: int) -> list[VectorItem]:
        _ = (embedding, top_k)
        raise NotImplementedError("Milvus search is reserved for Memory and RAG phases.")

    async def delete(self, ids: list[str]) -> None:
        _ = ids
        raise NotImplementedError("Milvus deletes are reserved for Memory and RAG phases.")
