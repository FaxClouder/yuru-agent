from fastapi.testclient import TestClient

from yuru_agent_api.main import create_app


def test_health_returns_service_metadata() -> None:
    client = TestClient(create_app())

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "yuru-agent-api",
        "version": "0.1.0",
    }


def test_database_health_uses_unified_response_shape() -> None:
    client = TestClient(create_app())

    response = client.get("/api/health/db")

    assert response.status_code in {200, 503}
    body = response.json()
    assert set(body) == {"success", "data", "error"}
    assert isinstance(body["success"], bool)
