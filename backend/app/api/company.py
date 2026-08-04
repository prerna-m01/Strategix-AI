from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.company import CompanyCreate, CompanyResponse
from backend.app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@router.get("/", response_model=list[CompanyResponse])
def get_companies(
    db: Session = Depends(get_db),
):
    service = CompanyService(db)
    return service.get_all_companies()


@router.post("/", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    service = CompanyService(db)

    return service.create_company(
        name=company.name,
        industry=company.industry,
        headquarters=company.headquarters,
        ceo=company.ceo,
    )