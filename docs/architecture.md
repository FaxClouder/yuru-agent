# YuruAgent Architecture

YuruAgent is organized as a monorepo so the frontend, backend, shared contracts,
and local infrastructure can evolve together.

```text
apps/web          Next.js workspace UI
apps/api          FastAPI service, API contracts, SQLAlchemy models
packages/shared   Reserved shared contracts package
infra/docker      Local PostgreSQL, pgvector, and Milvus services
docs              Roadmap, architecture, API, and development notes
```

## Runtime Shape

```text
Next.js frontend
  -> FastAPI backend
    -> PostgreSQL for structured business data
    -> Milvus interface reserved for vector retrieval
    -> LangGraph runner interface reserved for agent execution
```

PostgreSQL is the source of truth for structured records such as agents, runs,
steps, memory metadata, documents, tools, and workflows. Milvus is reserved for
embedding search in Memory and RAG phases. The first phase includes the
provider-neutral vector store contract but does not perform embedding writes.

## Current Design Progress

Implemented in Phase 0:

- `apps/web` contains the Next.js App Router workspace shell.
- `apps/api` contains the FastAPI app factory, route registration, unified API
  envelope, health checks, SQLAlchemy base model, and Alembic migration setup.
- `infra/docker/docker-compose.yml` defines PostgreSQL with pgvector and a
  standalone Milvus stack.
- `vectorstores/base.py` defines the provider-neutral vector store contract.
- `vectorstores/milvus.py` reserves the Milvus adapter boundary for later
  Memory and RAG phases.

Reserved for later phases:

- Phase 1 implements real `Agent` CRUD and frontend forms.
- Phase 2 implements LangGraph execution and run event streaming.
- Phase 4-6 implement memory extraction, RAG retrieval, and context assembly.
- Phase 7+ implement tools, workflows, templates, and evaluation.

Operational note:

- The backend can run without PostgreSQL for UI/API preview. `/api/health/db`
  reports the database state and returns `503` when PostgreSQL is not running.

## Backend Boundaries

- `api/routes`: HTTP routes and response contracts.
- `schemas`: Pydantic request and response models.
- `models`: SQLAlchemy persistence models.
- `core`: settings, database checks, logging, and error handling.
- `graph`: LangGraph execution boundary for Phase 2.
- `vectorstores`: Milvus or pgvector adapter boundary for Memory and RAG.

## Frontend Boundaries

- `src/app`: App Router pages and global styles.
- `src/components`: Reusable workspace UI components.
- `src/lib`: API client and browser-side helpers.

The first screen is the actual workspace shell, not a marketing landing page.
Reserved modules are visible as navigable placeholders so later phases have a
clear UI home.

## Code Comment Rules

- Public module boundaries should have short docstrings or focused comments.
- Comments should explain intent or phase boundaries, not restate obvious code.
- Reserved interfaces should name the phase that will implement behavior.
