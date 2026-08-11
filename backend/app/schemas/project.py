from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    project_id: str
    company_id: int
    client_id: int
    project_name: str
    description: str | None = None
    project_type: str
    status: str
    start_date: date
    end_date: date | None = None
    budget: Decimal


class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    project_id: str
    company_id: int
    client_id: int
    project_name: str
    description: str | None
    project_type: str
    status: str
    start_date: date
    end_date: date | None
    budget: Decimal