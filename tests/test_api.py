from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_test_endpoint_returns_placeholder_reply() -> None:
    response = client.post("/chat/test", json={"message": "hola"})
    assert response.status_code == 200
    assert response.json() == {"reply": "placeholder: hola"}


def test_chat_test_endpoint_validates_payload() -> None:
    response = client.post("/chat/test", json={"message": ""})
    assert response.status_code == 422


def test_swagger_docs_is_accessible() -> None:
    response = client.get("/docs")
    assert response.status_code == 200
