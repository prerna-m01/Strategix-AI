from datetime import date

from pydantic import BaseModel, ConfigDict


class ClientCreate(BaseModel):
    client_id: str
    company_id: int
    client_name: str
    industry: str
    contact_person: str
    email: str
    location: str
    contract_start_date: date
    contract_end_date: date | None = None
    annual_contract_value: float
    status: str = "active"


class ClientResponse(BaseModel):
    id: int
    client_id: str
    company_id: int
    client_name: str
    industry: str
    contact_person: str
    email: str
    location: str
    contract_start_date: date
    contract_end_date: date | None
    annual_contract_value: float
    status: str

    model_config = ConfigDict(
        from_attributes=True,
    )