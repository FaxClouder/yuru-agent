# API Contract

All `/api/*` endpoints use a stable response envelope:

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

## Health

```text
GET /health
GET /api/health/db
```

`GET /health` returns service metadata. `GET /api/health/db` runs a minimal
database query and returns `503` when the configured database is unavailable.

Current Phase 0 behavior:

```json
{
  "status": "ok",
  "service": "yuru-agent-api",
  "version": "0.1.0"
}
```

When PostgreSQL is not running, `/api/health/db` returns:

```json
{
  "success": false,
  "data": {
    "status": "unavailable"
  },
  "error": "<database connection details>"
}
```

## Agent Workspace

Reserved for Phase 1:

```text
GET    /api/agents
POST   /api/agents
GET    /api/agents/{agent_id}
PATCH  /api/agents/{agent_id}
DELETE /api/agents/{agent_id}
```

The first foundation phase defines the schema and route shape. Full persistence
and CRUD behavior belong to Phase 1.

Current Phase 0 behavior:

- `GET /api/agents` returns an empty list.
- Write/detail routes return reserved capability metadata.

## Agent Runner

Reserved for Phase 2:

```text
POST /api/agents/{agent_id}/runs
GET  /api/runs/{run_id}
GET  /api/runs/{run_id}/events
```

The route contract is present so the frontend and later LangGraph runner can
target stable paths.

Current Phase 0 behavior:

- Run creation returns HTTP `202` with `Phase 2 Agent Runner` reserved metadata.
- Run detail and event routes are present but do not execute LangGraph.

## Future Modules

```text
GET /api/memory
GET /api/knowledge-bases
GET /api/tools
```

These endpoints return reserved capability metadata until their roadmap phases
begin.

Current Phase 0 behavior:

- `/api/memory` is reserved for Phase 4.
- `/api/knowledge-bases` is reserved for Phase 5.
- `/api/tools` is reserved for Phase 7.
