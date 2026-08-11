from sqlalchemy.orm import configure_mappers

from backend.app.main import app
from backend.app.models import Project, Campaign
from backend.app.repositories.project_repository import ProjectRepository
from backend.app.repositories.campaign_repository import CampaignRepository
from backend.app.services.project_service import ProjectService
from backend.app.services.campaign_service import CampaignService
from backend.app.schemas.project import ProjectCreate, ProjectResponse
from backend.app.schemas.campaign import CampaignCreate, CampaignResponse


def test_project_campaign_integration():
    # SQLAlchemy models and relationships
    configure_mappers()

    assert Project.__tablename__ == "projects"
    assert Campaign.__tablename__ == "campaigns"

    # Repository layer
    assert ProjectRepository is not None
    assert CampaignRepository is not None

    # Service layer
    assert ProjectService is not None
    assert CampaignService is not None

    # Schema layer
    assert ProjectCreate is not None
    assert ProjectResponse is not None
    assert CampaignCreate is not None
    assert CampaignResponse is not None

    # FastAPI OpenAPI routes
    paths = app.openapi()["paths"]

    expected_routes = {
        "/api/v1/projects/",
        "/api/v1/projects/{project_id}",
        "/api/v1/projects/client/{client_id}",
        "/api/v1/projects/company/{company_id}",
        "/api/v1/campaigns/",
        "/api/v1/campaigns/{campaign_id}",
        "/api/v1/campaigns/project/{project_id}",
    }

    assert expected_routes.issubset(paths.keys())