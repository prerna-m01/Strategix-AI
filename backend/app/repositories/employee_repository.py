from sqlalchemy.orm import Session

from backend.app.models.employee import Employee


class EmployeeRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Employee).all()

    def get_by_id(self, employee_id: int):
        return (
            self.db.query(Employee)
            .filter(Employee.id == employee_id)
            .first()
        )

    def get_by_employee_code(self, employee_code: str):
        return (
            self.db.query(Employee)
            .filter(Employee.employee_id == employee_code)
            .first()
        )

    def get_by_email(self, email: str):
        return (
            self.db.query(Employee)
            .filter(Employee.email == email)
            .first()
        )

    def create(self, employee: Employee):
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)

        return employee