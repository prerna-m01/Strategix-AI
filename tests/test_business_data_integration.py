from fastapi.testclient import TestClient
from sqlalchemy.orm import configure_mappers

from backend.app.main import app
from backend.app.models.company import Company
from backend.app.models.department import Department
from backend.app.models.employee import Employee
from backend.app.models.business_kpi import BusinessKPI


client = TestClient(app)


def test_business_data_integration():

    # --------------------------------------------------
    # 1. SQLAlchemy mapper configuration
    # --------------------------------------------------
    configure_mappers()

    assert Company.__tablename__ == "companies"
    assert Department.__tablename__ == "departments"
    assert Employee.__tablename__ == "employees"
    assert BusinessKPI.__tablename__ == "business_kpis"

    # --------------------------------------------------
    # 2. Verify application imports
    # --------------------------------------------------
    assert app is not None

    # --------------------------------------------------
    # 3. Verify OpenAPI routes
    # --------------------------------------------------
    schema = app.openapi()
    paths = schema["paths"]

    expected_routes = [
        "/api/v1/companies/",
        "/api/v1/departments/",
        "/api/v1/employees/",
        "/api/v1/employees/{employee_id}",
        "/api/v1/employees/department/{department_id}",
        "/api/v1/business-kpis/",
        "/api/v1/projects/",
        "/api/v1/campaigns/",
    ]

    for route in expected_routes:
        assert route in paths, f"Missing route: {route}"

    # --------------------------------------------------
    # 4. Authentication layer verification
    # --------------------------------------------------
    protected_endpoints = [
        "/api/v1/companies/",
        "/api/v1/employees/",
        "/api/v1/business-kpis/",
        "/api/v1/projects/",
        "/api/v1/campaigns/",
    ]

    for endpoint in protected_endpoints:
        response = client.get(endpoint)

        assert response.status_code in (
            401,
            403,
        ), f"Unexpected status for {endpoint}: {response.status_code}"

    # --------------------------------------------------
    # 5. Health check
    # --------------------------------------------------
    response = client.get("/api/v1/health/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["database"] == "connected"