from sqlalchemy.orm import Session

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
    ValidationException,
)
from backend.app.core.logger import logger
from backend.app.models.company import Company
from backend.app.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self, db: Session):
        self.repository = CompanyRepository(db)

    def get_all_companies(self):
        """
        Return all companies.
        """
        logger.info("Fetching all companies")
        return self.repository.get_all()

    def get_company(self, company_id: int):
        """
        Return a company by ID.
        """
        logger.info(f"Fetching company with ID: {company_id}")

        company = self.repository.get_by_id(company_id)

        if not company:
            logger.warning(f"Company with ID {company_id} not found")
            raise ResourceNotFoundException("Company")

        return company

    def create_company(
        self,
        name: str,
        industry: str,
        headquarters: str,
        ceo: str,
    ):
        """
        Create a new company after validation.
        """

        # Validate input
        if not name.strip():
            raise ValidationException(
                "Company name cannot be empty."
            )

        # Check duplicate company
        existing_companies = self.repository.get_all()

        for existing_company in existing_companies:
            if existing_company.name.lower() == name.lower():
                logger.warning(
                    f"Duplicate company creation attempted: {name}"
                )
                raise DuplicateResourceException("Company")

        logger.info(f"Creating company: {name}")

        company = Company(
            name=name,
            industry=industry,
            headquarters=headquarters,
            ceo=ceo,
        )

        company = self.repository.create(company)

        logger.info(
            f"Company created successfully: {company.name}"
        )

        return company