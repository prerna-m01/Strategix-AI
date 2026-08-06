from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
)
from backend.app.services.department_service import DepartmentService

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db),
):
    service = DepartmentService(db)
    return service.get_all_departments()


@router.post("/", response_model=DepartmentResponse)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    service = DepartmentService(db)

    return service.create_department(
        name=department.name,
        description=department.description,
        company_id=department.company_id,
    )