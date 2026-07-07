from fastapi import FastAPI

from yuru_agent_api import __version__
from yuru_agent_api.api.router import api_router
from yuru_agent_api.core.errors import register_error_handlers


def create_app() -> FastAPI:
    """Create and configure the YuruAgent API application."""
    app = FastAPI(
        title="YuruAgent API",
        version=__version__,
        summary="Backend API for the YuruAgent personal automation workspace.",
    )
    register_error_handlers(app)
    app.include_router(api_router)

    @app.get("/health", tags=["health"])
    def health() -> dict[str, str]:
        return {
            "status": "ok",
            "service": "yuru-agent-api",
            "version": __version__,
        }

    return app


app = create_app()
