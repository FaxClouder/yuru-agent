from dataclasses import dataclass


@dataclass(frozen=True)
class GraphRunInput:
    agent_id: str
    user_task: str


class GraphRunner:
    """Reserved LangGraph runner interface for Phase 2 Agent Runner."""

    async def run(self, payload: GraphRunInput) -> str:
        _ = payload
        raise NotImplementedError("Graph execution is reserved for Phase 2 Agent Runner.")
