from sqlalchemy.orm import Session

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
    ValidationException,
)
from backend.app.core.logger import logger
from backend.app.models.employee import Employee
from backend.app.repositories.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self, db: Session):
        self.repository = EmployeeRepository(db)

    def get_all_employees(self):
        logger.info("Fetching all employees")

        return self.repository.get_all()

    def get_employee(self, employee_id: int):
        logger.info(
            f"Fetching employee with ID: {employee_id}"
        )

        employee = self.repository.get_by_id(employee_id)

        if not employee:
            logger.warning(
                f"Employee with ID {employee_id} not found"
            )

            raise ResourceNotFoundException("Employee")

        return employee

    def create_employee(
        self,
        employee_id: str,
        full_name: str,
        email: str,
        department_id: int,
        job_title: str,
        location: str,
        employment_type: str,
        hire_date,
        annual_salary: float,
    ):
        if not employee_id.strip():
            raise ValidationException(
                "Employee ID cannot be empty."
            )

        if not full_name.strip():
            raise ValidationException(
                "Employee name cannot be empty."
            )

        if not email.strip():
            raise ValidationException(
                "Employee email cannot be empty."
            )

        existing_employee = (
            self.repository.get_by_employee_code(employee_id)
        )

        if existing_employee:
            logger.warning(
                f"Duplicate employee ID attempted: {employee_id}"
            )

            raise DuplicateResourceException("Employee")

        existing_email = self.repository.get_by_email(email)

        if existing_email:
            logger.warning(
                f"Duplicate employee email attempted: {email}"
            )

            raise DuplicateResourceException("Employee")

        logger.info(
            f"Creating employee: {employee_id}"
        )

        employee = Employee(
            employee_id=employee_id,
            full_name=full_name,
            email=email,
            department_id=department_id,
            job_title=job_title,
            location=location,
            employment_type=employment_type,
            hire_date=hire_date,
            annual_salary=annual_salary,
        )

        employee = self.repository.create(employee)

        logger.info(
            f"Employee created successfully: {employee.employee_id}"
        )

        return employee
    def get_company_employees(self, company_id: int):
        return self.repository.get_by_company(
        company_id=company_id,
    )
    def get_department_employees(self, department_id: int):
        logger.info(
            f"Fetching employees for department: {department_id}"
        )

        return self.repository.get_by_department(
            department_id=department_id
        )