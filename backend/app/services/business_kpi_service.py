from sqlalchemy.orm import Session

from backend.app.models import BusinessKPI
from backend.app.repositories.business_kpi_repository import (
    BusinessKPIRepository,
)


class BusinessKPIService:

    def __init__(self, db: Session):
        self.repository = BusinessKPIRepository(db)

    def get_all_kpis(self):
        return self.repository.get_all()

    def get_department_kpis(self, department_id: int):
        return self.repository.get_by_department(department_id)

    def create_kpi(
        self,
        metric_name: str,
        metric_value: float,
        unit: str,
        year: int,
        department_id: int,
    ):
        kpi = BusinessKPI(
            metric_name=metric_name,
            metric_value=metric_value,
            unit=unit,
            year=year,
            department_id=department_id,
        )

        return self.repository.create(kpi)