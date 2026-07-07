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
If Docker is not installed or not available on PATH, the frontend and backend can
still run for UI/API preview, but `/api/health/db` will return `503`.

## Backend

```powershell
uv run --project apps/api uvicorn yuru_agent_api.main:app --reload --app-dir apps/api/src
```

If port `8000` is already in use:

```powershell
uv run --project apps/api uvicorn yuru_agent_api.main:app --reload --app-dir apps/api/src --host 127.0.0.1 --port 8002
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

To point the frontend at a non-default backend port:

```powershell
$env:NEXT_PUBLIC_API_BASE_URL='http://127.0.0.1:8002'
pnpm --dir apps/web dev --hostname 127.0.0.1 --port 3000
```

Useful checks:

```powershell
pnpm --dir apps/web test
pnpm --dir apps/web build
```

## Current Phase 0 Verification

The following checks passed after the foundation scaffold was implemented:

```text
uv run --project apps/api pytest       5 passed
uv run --project apps/api ruff check . passed
pnpm --dir apps/web test               1 passed
pnpm --dir apps/web build              passed
```

Local preview endpoints:

```text
Frontend: http://127.0.0.1:3000
Backend:  http://127.0.0.1:8002
Health:   http://127.0.0.1:8002/health
```

## Phase Rules

- Phase 0 owns framework, tooling, health checks, and reserved interfaces.
- Phase 1 owns real Agent CRUD behavior.
- Phase 2 owns LangGraph execution and streaming run events.
- Memory, RAG, tools, workflows, and evaluation should stay behind reserved
  interfaces until their roadmap phase begins.
