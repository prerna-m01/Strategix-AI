from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_get_employees_requires_authentication():
    response = client.get("/api/v1/employees/")

    assert response.status_code == 401