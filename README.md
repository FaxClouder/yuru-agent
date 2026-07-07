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

Run the frontend:

```powershell
pnpm --dir apps/web dev
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
