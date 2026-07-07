# Development Guide

## Prerequisites

- Node.js with `pnpm`
- Python 3.11+ with `uv`
- Docker, for local PostgreSQL and Milvus services

## Install Dependencies

```powershell
pnpm install
uv sync --project apps/api --dev
```

## Local Services

```powershell
docker compose -f infra/docker/docker-compose.yml up -d
```

The compose file starts PostgreSQL with pgvector and a standalone Milvus stack.

## Backend

```powershell
uv run --project apps/api uvicorn yuru_agent_api.main:app --reload --app-dir apps/api/src
```

Useful checks:

```powershell
uv run --project apps/api pytest
uv run --project apps/api ruff check .
uv run --project apps/api alembic upgrade head
```

## Frontend

```powershell
pnpm --dir apps/web dev
```

Useful checks:

```powershell
pnpm --dir apps/web test
pnpm --dir apps/web build
```

## Phase Rules

- Phase 0 owns framework, tooling, health checks, and reserved interfaces.
- Phase 1 owns real Agent CRUD behavior.
- Phase 2 owns LangGraph execution and streaming run events.
- Memory, RAG, tools, workflows, and evaluation should stay behind reserved
  interfaces until their roadmap phase begins.
