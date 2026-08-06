from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_companies():
    response = client.get("/api/v1/companies/")
    assert response.status_code == 200