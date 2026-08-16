from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.business_kpi import (
    BusinessKPICreate,
    BusinessKPIResponse,
)
from backend.app.services.business_kpi_service import (
    BusinessKPIService,
)

router = APIRouter(
    prefix="/business-kpis",
    tags=["Business KPIs"],
)


@router.get(
    "/",
    response_model=list[BusinessKPIResponse],
)
def get_business_kpis(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = BusinessKPIService(db)

    return service.get_all_kpis()


@router.get(
    "/department/{department_id}",
    response_model=list[BusinessKPIResponse],
)
def get_department_business_kpis(
    department_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = BusinessKPIService(db)

    return service.get_department_kpis(
        department_id=department_id,
    )


@router.post(
    "/",
    response_model=BusinessKPIResponse,
)
def create_business_kpi(
    kpi: BusinessKPICreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = BusinessKPIService(db)

    return service.create_kpi(
        metric_name=kpi.metric_name,
        metric_value=kpi.metric_value,
        unit=kpi.unit,
        year=kpi.year,
        department_id=kpi.department_id,
    )