from sqlalchemy.orm import Session

from backend.app.models.project import Project


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Project).all()

    def get_by_id(self, project_id: int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def get_by_project_id(self, project_id: str):
        return (
            self.db.query(Project)
            .filter(Project.project_id == project_id)
            .first()
        )

    def get_by_client_id(self, client_id: int):
        return (
            self.db.query(Project)
            .filter(Project.client_id == client_id)
            .all()
        )

    def get_by_company_id(self, company_id: int):
        return (
            self.db.query(Project)
            .filter(Project.company_id == company_id)
            .all()
        )

    def create(self, project: Project):
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def update(self, project: Project):
        self.db.commit()
        self.db.refresh(project)

        return project

    def delete(self, project: Project):
        self.db.delete(project)
        self.db.commit()

        return True