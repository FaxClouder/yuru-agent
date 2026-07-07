from fastapi.testclient import TestClient

from yuru_agent_api.main import create_app


def test_agent_workspace_routes_are_reserved_with_consistent_shape() -> None:
    client = TestClient(create_app())

    response = client.get("/api/agents")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "data": [],
        "error": None,
    }


def test_future_module_routes_return_reserved_metadata() -> None:
    client = TestClient(create_app())

    endpoints = [
        "/api/memory",
        "/api/knowledge-bases",
        "/api/tools",
    ]

    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.status_code == 200
        body = response.json()
        assert body["success"] is True
        assert body["error"] is None
        assert body["data"]["status"] == "reserved"


def test_run_creation_route_is_reserved_for_agent_runner_phase() -> None:
    client = TestClient(create_app())

    response = client.post(
        "/api/agents/00000000-0000-0000-0000-000000000001/runs",
        json={"user_task": "Summarize today's notes."},
    )

    assert response.status_code == 202
    assert response.json()["data"] == {
        "status": "reserved",
        "phase": "Phase 2 Agent Runner",
    }
