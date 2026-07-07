# YuruAgent

YuruAgent is a personal automation agent workspace for building, running, and observing extensible AI agents.

## Vision

YuruAgent aims to grow from a simple agent runner into a general-purpose workspace for personal automation:

- Create and manage reusable AI agents.
- Connect tools such as browser automation, files, search, calendars, email, and knowledge bases.
- Compose agent workflows with steps, branches, retries, and human approval.
- Observe agent runs through traces, tool-call logs, costs, and execution history.

## Planned Modules

- Agent workspace
- Workflow builder
- Tool registry
- Knowledge base and RAG
- Browser automation agent
- Research agent template
- Developer assistant template
- Agent run tracing and evaluation

## Status

The repository now contains the Phase 0 project foundation:

- Next.js workspace shell in `apps/web`.
- FastAPI backend scaffold in `apps/api`.
- PostgreSQL + pgvector and Milvus local service definitions in `infra/docker`.
- Reserved API contracts for agents, runs, memory, RAG, and tools.
- SQLAlchemy 2.x model foundation and Alembic migration setup.

Phase 1 will implement the real Agent Workspace CRUD loop.

## Current Progress

The Phase 0 scaffold landed in commit `4ab4952` and is available on
`origin/main`.

Completed:

- Frontend and backend project skeletons are runnable locally.
- Backend exposes `/health`, `/api/health/db`, and reserved module APIs.
- Frontend renders the first workspace screen with reserved module navigation.
- SQLAlchemy 2.x, Alembic, and the minimal `agents` table migration are in place.
- PostgreSQL + pgvector and Milvus local infrastructure is defined in Docker
  Compose.
- Phase documentation, API contracts, and development notes are available in
  `docs/`.

Current limitations:

- Agent CRUD is intentionally reserved for Phase 1.
- LangGraph execution is intentionally reserved for Phase 2.
- Memory, RAG, tools, and workflows are interface placeholders only.
- Database health returns `503` until local PostgreSQL is started.

## Quick Start

Install dependencies:

```powershell
pnpm install
uv sync --project apps/api --dev
```

Start local infrastructure:

```powershell
docker compose -f infra/docker/docker-compose.yml up -d
```

Run the backend:

```powershell
uv run --project apps/api uvicorn yuru_agent_api.main:app --reload --app-dir apps/api/src
```

If port `8000` is occupied, use another port:

```powershell
uv run --project apps/api uvicorn yuru_agent_api.main:app --reload --app-dir apps/api/src --host 127.0.0.1 --port 8002
```

Run the frontend:

```powershell
pnpm --dir apps/web dev
```

Local preview used during Phase 0 verification:

```text
Frontend: http://127.0.0.1:3000
Backend:  http://127.0.0.1:8002
```

Run checks:

```powershell
uv run --project apps/api pytest
pnpm --dir apps/web test
pnpm --dir apps/web build
```

## Documentation

- [Roadmap and Phase Plan](docs/ROADMAP.md)
- [Architecture](docs/architecture.md)
- [API Contract](docs/api-contract.md)
- [Development Guide](docs/dev-guide.md)

## License

MIT
