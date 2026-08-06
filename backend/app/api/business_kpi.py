from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
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


@router.get("/", response_model=list[BusinessKPIResponse])
def get_business_kpis(
    db: Session = Depends(get_db),
):
    service = BusinessKPIService(db)
    return service.get_all_kpis()


@router.post("/", response_model=BusinessKPIResponse)
def create_business_kpi(
    kpi: BusinessKPICreate,
    db: Session = Depends(get_db),
):
    service = BusinessKPIService(db)

    return service.create_kpi(
        metric_name=kpi.metric_name,
        metric_value=kpi.metric_value,
        unit=kpi.unit,
        year=kpi.year,
        department_id=kpi.department_id,
    )