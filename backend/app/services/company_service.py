from sqlalchemy.orm import Session

from backend.app.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self, db: Session):
        self.repository = CompanyRepository(db)

    def get_all_companies(self):
        return self.repository.get_all()

    def get_company(self, company_id: int):
        return self.repository.get_by_id(company_id)

    def create_company(
        self,
        name: str,
        industry: str,
        headquarters: str,
        ceo: str,
    ):
        return self.repository.create(
            name=name,
            industry=industry,
            headquarters=headquarters,
            ceo=ceo,
        )