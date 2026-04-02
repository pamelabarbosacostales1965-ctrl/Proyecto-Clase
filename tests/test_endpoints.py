from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Calculator API is running"}


def test_suma_endpoint() -> None:
    response = client.post("/suma", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_resta_endpoint() -> None:
    response = client.post("/resta", json={"a": 8, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_multiplicacion_endpoint() -> None:
    response = client.post("/multiplicacion", json={"a": 4, "b": 5})

    assert response.status_code == 200
    assert response.json() == {"result": 20}