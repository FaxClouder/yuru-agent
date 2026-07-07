from fastapi import APIRouter

from yuru_agent_api.api.routes import agents, health, memory, rag, runs, tools

api_router = APIRouter(prefix="/api")
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(runs.router, tags=["runs"])
api_router.include_router(memory.router, prefix="/memory", tags=["memory"])
api_router.include_router(rag.router, prefix="/knowledge-bases", tags=["knowledge-bases"])
api_router.include_router(tools.router, prefix="/tools", tags=["tools"])
