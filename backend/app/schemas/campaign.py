from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CampaignCreate(BaseModel):
    campaign_id: str
    project_id: int
    campaign_name: str
    campaign_type: str
    status: str
    start_date: date
    end_date: date | None = None
    budget: Decimal
    revenue_generated: Decimal


class CampaignResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    campaign_id: str
    project_id: int
    campaign_name: str
    campaign_type: str
    status: str
    start_date: date
    end_date: date | None
    budget: Decimal
    revenue_generated: Decimal