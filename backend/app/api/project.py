from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
)
from backend.app.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.get(
    "/",
    response_model=list[ProjectResponse],
)
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.get_all_projects()


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.get_project(project_id)


@router.get(
    "/client/{client_id}",
    response_model=list[ProjectResponse],
)
def get_projects_by_client(
    client_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.get_projects_by_client(client_id)


@router.get(
    "/company/{company_id}",
    response_model=list[ProjectResponse],
)
def get_projects_by_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.get_projects_by_company(company_id)


@router.post(
    "/",
    response_model=ProjectResponse,
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.create_project(
        project_id=project.project_id,
        company_id=project.company_id,
        client_id=project.client_id,
        project_name=project.project_name,
        description=project.description,
        project_type=project.project_type,
        status=project.status,
        start_date=project.start_date,
        end_date=project.end_date,
        budget=project.budget,
    )


@router.delete(
    "/{project_id}",
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ProjectService(db)

    return service.delete_project(project_id)