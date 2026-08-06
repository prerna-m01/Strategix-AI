from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_business_kpis():
    response = client.get("/api/v1/business-kpis/")
    assert response.status_code == 200