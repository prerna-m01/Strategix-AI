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
        logger.info(
            f"Fetching company with ID: {company_id}"
        )

        company = self.repository.get_by_id(company_id)

        if not company:
            logger.warning(
                f"Company with ID {company_id} not found"
            )

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
        Create a new company.
        """

        name = name.strip()
        industry = industry.strip()
        headquarters = headquarters.strip()
        ceo = ceo.strip()

        if not name:
            raise ValidationException(
                "Company name cannot be empty."
            )

        if not industry:
            raise ValidationException(
                "Company industry cannot be empty."
            )

        if not headquarters:
            raise ValidationException(
                "Company headquarters cannot be empty."
            )

        if not ceo:
            raise ValidationException(
                "Company CEO cannot be empty."
            )

        existing_company = self.repository.get_by_name(name)

        if existing_company:
            logger.warning(
                f"Duplicate company creation attempted: {name}"
            )

            raise DuplicateResourceException("Company")

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

    def update_company(
        self,
        company_id: int,
        name: str | None = None,
        industry: str | None = None,
        headquarters: str | None = None,
        ceo: str | None = None,
    ):
        """
        Update an existing company.
        """

        company = self.get_company(company_id)

        if name is not None:
            name = name.strip()

            if not name:
                raise ValidationException(
                    "Company name cannot be empty."
                )

            existing_company = self.repository.get_by_name(name)

            if (
                existing_company
                and existing_company.id != company_id
            ):
                raise DuplicateResourceException("Company")

            company.name = name

        if industry is not None:
            industry = industry.strip()

            if not industry:
                raise ValidationException(
                    "Company industry cannot be empty."
                )

            company.industry = industry

        if headquarters is not None:
            headquarters = headquarters.strip()

            if not headquarters:
                raise ValidationException(
                    "Company headquarters cannot be empty."
                )

            company.headquarters = headquarters

        if ceo is not None:
            ceo = ceo.strip()

            if not ceo:
                raise ValidationException(
                    "Company CEO cannot be empty."
                )

            company.ceo = ceo

        company = self.repository.update(company)

        logger.info(
            f"Company {company_id} updated successfully"
        )

        return company

    def delete_company(self, company_id: int):
        """
        Delete a company.
        """

        company = self.get_company(company_id)

        self.repository.delete(company)

        logger.info(
            f"Company {company_id} deleted successfully"
        )

        return True