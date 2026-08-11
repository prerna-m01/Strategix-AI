from datetime import date
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.models.project import Project
from backend.app.repositories.project_repository import ProjectRepository


class ProjectService:
    def __init__(self, db: Session):
        self.repository = ProjectRepository(db)

    def get_all_projects(self):
        return self.repository.get_all()

    def get_project(self, project_id: int):
        project = self.repository.get_by_id(project_id)

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        return project

    def get_projects_by_client(self, client_id: int):
        return self.repository.get_by_client_id(client_id)

    def get_projects_by_company(self, company_id: int):
        return self.repository.get_by_company_id(company_id)

    def create_project(
        self,
        project_id: str,
        company_id: int,
        client_id: int,
        project_name: str,
        description: str | None,
        project_type: str,
        status: str,
        start_date: date,
        end_date: date | None,
        budget: Decimal,
    ):
        existing = self.repository.get_by_project_id(project_id)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Project ID already exists",
            )

        project = Project(
            project_id=project_id,
            company_id=company_id,
            client_id=client_id,
            project_name=project_name,
            description=description,
            project_type=project_type,
            status=status,
            start_date=start_date,
            end_date=end_date,
            budget=budget,
        )

        return self.repository.create(project)

    def delete_project(self, project_id: int):
        project = self.get_project(project_id)

        self.repository.delete(project)

        return {"message": "Project deleted successfully"}