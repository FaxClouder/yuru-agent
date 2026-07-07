# Phase 0 Project Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the YuruAgent project foundation with runnable frontend, backend, database configuration, reserved APIs, and engineering documentation.

**Architecture:** Use a monorepo with `apps/web` for Next.js, `apps/api` for FastAPI, `packages/shared` for future shared contracts, and `infra/docker` for local services. The backend exposes health and reserved module APIs while keeping business behavior minimal for later phases.

**Tech Stack:** Next.js, TypeScript, FastAPI, SQLAlchemy 2.x, Alembic, PostgreSQL, Milvus-ready vector store interface, pnpm, uv, pytest, Vitest.

---

### Task 1: Backend Foundation

**Files:**
- Create: `apps/api/pyproject.toml`
- Create: `apps/api/src/yuru_agent_api/main.py`
- Create: `apps/api/src/yuru_agent_api/api/routes/*.py`
- Create: `apps/api/src/yuru_agent_api/core/*.py`
- Create: `apps/api/tests/*.py`

- [x] **Step 1: Write failing API tests**

Run: `uv run --project apps/api pytest`
Expected: FAIL because the API package and routes do not exist.

- [x] **Step 2: Implement minimal FastAPI app**

Add app factory, router registration, health checks, unified response models, and reserved route handlers.

- [x] **Step 3: Run backend tests**

Run: `uv run --project apps/api pytest`
Expected: PASS.

### Task 2: Frontend Foundation

**Files:**
- Create: `apps/web/package.json`
- Create: `apps/web/src/app/page.tsx`
- Create: `apps/web/src/app/layout.tsx`
- Create: `apps/web/src/components/*.tsx`
- Create: `apps/web/tests/*.test.tsx`

- [x] **Step 1: Write failing UI smoke tests**

Run: `pnpm --dir apps/web test`
Expected: FAIL because frontend package and components do not exist.

- [x] **Step 2: Implement minimal workspace shell**

Add App Router layout, dashboard page, reserved navigation, and API client placeholder.

- [x] **Step 3: Run frontend tests and build**

Run: `pnpm --dir apps/web test`
Run: `pnpm --dir apps/web build`
Expected: PASS.

### Task 3: Infrastructure and Documentation

**Files:**
- Create: `.env.example`
- Create: `pnpm-workspace.yaml`
- Create: `package.json`
- Create: `infra/docker/docker-compose.yml`
- Create: `docs/architecture.md`
- Create: `docs/api-contract.md`
- Create: `docs/dev-guide.md`
- Modify: `README.md`

- [x] **Step 1: Add root workspace and infra files**

Define pnpm workspaces, local PostgreSQL + Milvus services, and shared environment variables.

- [x] **Step 2: Document architecture and development flow**

Describe module boundaries, reserved interfaces, local startup, and phase rules.

- [x] **Step 3: Verify repository**

Run: `uv run --project apps/api pytest`
Run: `pnpm --dir apps/web test`
Run: `pnpm --dir apps/web build`
Run: `git diff --check`
Expected: all commands pass.
