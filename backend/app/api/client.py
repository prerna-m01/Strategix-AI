from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.client import (
    ClientCreate,
    ClientResponse,
)
from backend.app.services.client_service import ClientService


router = APIRouter(
    prefix="/clients",
    tags=["Clients"],
)


@router.get(
    "/",
    response_model=list[ClientResponse],
)
def get_clients(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ClientService(db)

    return service.get_all_clients()


@router.get(
    "/{client_id}",
    response_model=ClientResponse,
)
def get_client(
    client_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ClientService(db)

    return service.get_client(client_id)


@router.post(
    "/",
    response_model=ClientResponse,
)
def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = ClientService(db)

    return service.create_client(
        client_id=client.client_id,
        company_id=client.company_id,
        client_name=client.client_name,
        industry=client.industry,
        contact_person=client.contact_person,
        email=client.email,
        location=client.location,
        contract_start_date=client.contract_start_date,
        contract_end_date=client.contract_end_date,
        annual_contract_value=client.annual_contract_value,
        status=client.status,
    )