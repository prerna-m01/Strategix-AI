from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.auth.dependencies import get_current_user
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.schemas.campaign import (
    CampaignCreate,
    CampaignResponse,
)
from backend.app.services.campaign_service import CampaignService


router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"],
)


@router.get(
    "/",
    response_model=list[CampaignResponse],
)
def get_campaigns(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CampaignService(db)

    return service.get_all_campaigns()


@router.get(
    "/{campaign_id}",
    response_model=CampaignResponse,
)
def get_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CampaignService(db)

    return service.get_campaign(campaign_id)


@router.get(
    "/project/{project_id}",
    response_model=list[CampaignResponse],
)
def get_campaigns_by_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CampaignService(db)

    return service.get_campaigns_by_project(project_id)


@router.post(
    "/",
    response_model=CampaignResponse,
)
def create_campaign(
    campaign: CampaignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CampaignService(db)

    return service.create_campaign(
        campaign_id=campaign.campaign_id,
        project_id=campaign.project_id,
        campaign_name=campaign.campaign_name,
        campaign_type=campaign.campaign_type,
        status=campaign.status,
        start_date=campaign.start_date,
        end_date=campaign.end_date,
        budget=campaign.budget,
        revenue_generated=campaign.revenue_generated,
    )


@router.delete(
    "/{campaign_id}",
)
def delete_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = CampaignService(db)

    return service.delete_campaign(campaign_id)