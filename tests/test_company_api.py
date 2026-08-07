from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.auth.jwt import create_access_token


client = TestClient(app)


def test_get_companies():
    token = create_access_token(
        {"sub": "admin@strategix.ai"}
    )

    response = client.get(
        "/api/v1/companies/",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200