from datetime import date

from sqlalchemy.orm import Session

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
    ValidationException,
)
from backend.app.core.logger import logger
from backend.app.models.client import Client
from backend.app.repositories.client_repository import ClientRepository


class ClientService:

    def __init__(self, db: Session):
        self.repository = ClientRepository(db)

    def get_all_clients(self):
        logger.info("Fetching all clients")

        return self.repository.get_all()

    def get_client(self, client_id: int):
        logger.info(
            f"Fetching client with ID: {client_id}"
        )

        client = self.repository.get_by_id(client_id)

        if not client:
            logger.warning(
                f"Client with ID {client_id} not found"
            )
            raise ResourceNotFoundException("Client")

        return client

    def create_client(
        self,
        client_id: str,
        company_id: int,
        client_name: str,
        industry: str,
        contact_person: str,
        email: str,
        location: str,
        contract_start_date: date,
        contract_end_date: date | None,
        annual_contract_value: float,
        status: str,
    ):
        if not client_id.strip():
            raise ValidationException(
                "Client ID cannot be empty."
            )

        if not client_name.strip():
            raise ValidationException(
                "Client name cannot be empty."
            )

        if annual_contract_value < 0:
            raise ValidationException(
                "Annual contract value cannot be negative."
            )

        existing_client = (
            self.repository.get_by_client_id(client_id)
        )

        if existing_client:
            logger.warning(
                f"Duplicate client ID attempted: {client_id}"
            )
            raise DuplicateResourceException("Client")

        existing_email = (
            self.repository.get_by_email(email)
        )

        if existing_email:
            logger.warning(
                f"Duplicate client email attempted: {email}"
            )
            raise DuplicateResourceException("Client")

        if (
            contract_end_date is not None
            and contract_end_date < contract_start_date
        ):
            raise ValidationException(
                "Contract end date cannot be before contract start date."
            )

        logger.info(
            f"Creating client: {client_name}"
        )

        client = Client(
            client_id=client_id,
            company_id=company_id,
            client_name=client_name,
            industry=industry,
            contact_person=contact_person,
            email=email,
            location=location,
            contract_start_date=contract_start_date,
            contract_end_date=contract_end_date,
            annual_contract_value=annual_contract_value,
            status=status,
        )

        client = self.repository.create(client)

        logger.info(
            f"Client created successfully: {client.client_name}"
        )

        return client