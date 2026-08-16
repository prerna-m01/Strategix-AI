from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_employee_routes_require_authentication():
    endpoints = [
        "/api/v1/employees/",
        "/api/v1/employees/1",
    ]

    for endpoint in endpoints:
        response = client.get(endpoint)

        assert response.status_code in (401, 403)

def test_department_employee_route_requires_authentication():
    response = client.get(
        "/api/v1/employees/department/1"
    )

    assert response.status_code in (401, 403)