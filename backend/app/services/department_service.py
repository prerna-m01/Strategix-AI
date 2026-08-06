from sqlalchemy.orm import Session

from backend.app.models.department import Department
from backend.app.repositories.department_repository import DepartmentRepository


class DepartmentService:

    def __init__(self, db: Session):
        self.repository = DepartmentRepository(db)

    def get_all_departments(self):
        return self.repository.get_all()

    def create_department(
        self,
        name: str,
        description: str,
        company_id: int,
    ):
        department = Department(
            name=name,
            description=description,
            company_id=company_id,
        )

        return self.repository.create(department)