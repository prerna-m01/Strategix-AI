from sqlalchemy.orm import Session

from backend.app.models import Department


class DepartmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Department).all()

    def create(self, department: Department):
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)
        return department