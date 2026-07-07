from dataclasses import dataclass

from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from yuru_agent_api.core.config import get_settings


@dataclass(frozen=True)
class DatabaseCheck:
    ok: bool
    error: str | None = None


def check_database() -> DatabaseCheck:
    """Run a minimal query against the configured PostgreSQL database."""
    settings = get_settings()
    try:
        engine = create_engine(settings.database_url, connect_args={"connect_timeout": 1})
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        return DatabaseCheck(ok=False, error=str(exc))

    return DatabaseCheck(ok=True)
