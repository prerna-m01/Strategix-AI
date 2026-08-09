from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
)
from backend.app.services.employee_service import EmployeeService


router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_employees(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = EmployeeService(db)

    return service.get_all_employees()


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = EmployeeService(db)

    return service.get_employee(employee_id)


@router.post(
    "/",
    response_model=EmployeeResponse,
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = EmployeeService(db)

    return service.create_employee(
        employee_id=employee.employee_id,
        full_name=employee.full_name,
        email=employee.email,
        department_id=employee.department_id,
        job_title=employee.job_title,
        location=employee.location,
        employment_type=employee.employment_type,
        hire_date=employee.hire_date,
        annual_salary=employee.annual_salary,
    )