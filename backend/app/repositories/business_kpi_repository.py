from sqlalchemy.orm import Session

from backend.app.models import BusinessKPI


class BusinessKPIRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(BusinessKPI).all()

    def get_by_department(self, department_id: int):
        return (
            self.db.query(BusinessKPI)
            .filter(BusinessKPI.department_id == department_id)
            .all()
        )

    def create(self, business_kpi: BusinessKPI):
        self.db.add(business_kpi)
        self.db.commit()
        self.db.refresh(business_kpi)
        return business_kpi