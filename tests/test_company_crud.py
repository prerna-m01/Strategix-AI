from backend.app.main import app
from backend.app.auth.jwt import create_access_token
from fastapi.testclient import TestClient


client = TestClient(app)


def get_auth_headers():
    token = create_access_token(
        {"sub": "admin@strategix.ai"}
    )

    return {
        "Authorization": f"Bearer {token}"
    }


def test_get_company_by_id():
    response = client.get(
        "/api/v1/companies/1",
        headers=get_auth_headers(),
    )

    assert response.status_code in [200, 404]


def test_get_company_requires_authentication():
    response = client.get(
        "/api/v1/companies/1"
    )

    assert response.status_code in [401, 403]


def test_create_company_validation():
    response = client.post(
        "/api/v1/companies/",
        headers=get_auth_headers(),
        json={
            "name": "",
            "industry": "Technology",
            "headquarters": "Delhi",
            "ceo": "Test CEO",
        },
    )

    assert response.status_code == 422


def test_update_company_requires_authentication():
    response = client.put(
        "/api/v1/companies/1",
        json={
            "industry": "Technology"
        },
    )

    assert response.status_code in [401, 403]


def test_delete_company_requires_authentication():
    response = client.delete(
        "/api/v1/companies/1"
    )

    assert response.status_code in [401, 403]