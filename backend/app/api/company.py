from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
    CompanyUpdate,
)
from backend.app.services.company_service import CompanyService


router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@router.get(
    "/",
    response_model=list[CompanyResponse],
)
def get_companies(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CompanyService(db)

    return service.get_all_companies()


@router.get(
    "/{company_id}",
    response_model=CompanyResponse,
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CompanyService(db)

    return service.get_company(company_id)


@router.post(
    "/",
    response_model=CompanyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CompanyService(db)

    return service.create_company(
        name=company.name,
        industry=company.industry,
        headquarters=company.headquarters,
        ceo=company.ceo,
    )


@router.put(
    "/{company_id}",
    response_model=CompanyResponse,
)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CompanyService(db)

    return service.update_company(
        company_id=company_id,
        name=company.name,
        industry=company.industry,
        headquarters=company.headquarters,
        ceo=company.ceo,
    )


@router.delete(
    "/{company_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CompanyService(db)

    service.delete_company(company_id)

    return None