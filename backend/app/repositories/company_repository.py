from sqlalchemy.orm import Session

from backend.app.models.company import Company


class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Company).all()

    def get_by_id(self, company_id: int):
        return (
            self.db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    def create(
        self,
        name: str,
        industry: str,
        headquarters: str,
        ceo: str,
    ):

        company = Company(
            name=name,
            industry=industry,
            headquarters=headquarters,
            ceo=ceo,
        )

        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)

        return company