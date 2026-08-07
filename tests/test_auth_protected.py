from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_companies_requires_authentication():
    response = client.get("/api/v1/companies/")

    assert response.status_code in [401, 403]