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

## Agent Runner

Reserved for Phase 2:

```text
POST /api/agents/{agent_id}/runs
GET  /api/runs/{run_id}
GET  /api/runs/{run_id}/events
```

The route contract is present so the frontend and later LangGraph runner can
target stable paths.

## Future Modules

```text
GET /api/memory
GET /api/knowledge-bases
GET /api/tools
```

These endpoints return reserved capability metadata until their roadmap phases
begin.
