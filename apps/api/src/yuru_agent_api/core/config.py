from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "YuruAgent API"
    api_cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])
    database_url: str = "postgresql+psycopg://yuru:yuru@localhost:5432/yuru_agent"
    milvus_uri: str = "http://localhost:19530"
    vector_store_provider: str = "milvus"


@lru_cache
def get_settings() -> Settings:
    """Return cached process settings."""
    return Settings()
