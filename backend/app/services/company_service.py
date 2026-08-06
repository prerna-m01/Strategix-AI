from sqlalchemy.orm import Session

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ValidationException,
)
from backend.app.models.company import Company
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
        # Validation
        if not name.strip():
            raise ValidationException(
                "Company name cannot be empty."
            )

        # Duplicate check
        existing_companies = self.repository.get_all()

        for company in existing_companies:
            if company.name.lower() == name.lower():
                raise DuplicateResourceException("Company")

        company = Company(
            name=name,
            industry=industry,
            headquarters=headquarters,
            ceo=ceo,
        )

        return self.repository.create(company)