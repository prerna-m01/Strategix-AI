from datetime import date
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.models.campaign import Campaign
from backend.app.repositories.campaign_repository import CampaignRepository


class CampaignService:
    def __init__(self, db: Session):
        self.repository = CampaignRepository(db)

    def get_all_campaigns(self):
        return self.repository.get_all()

    def get_campaign(self, campaign_id: int):
        campaign = self.repository.get_by_id(campaign_id)

        if not campaign:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Campaign not found",
            )

        return campaign

    def get_campaigns_by_project(self, project_id: int):
        return self.repository.get_by_project_id(project_id)

    def create_campaign(
        self,
        campaign_id: str,
        project_id: int,
        campaign_name: str,
        campaign_type: str,
        status: str,
        start_date: date,
        end_date: date | None,
        budget: Decimal,
        revenue_generated: Decimal,
    ):
        existing = self.repository.get_by_campaign_id(campaign_id)

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Campaign ID already exists",
            )

        campaign = Campaign(
            campaign_id=campaign_id,
            project_id=project_id,
            campaign_name=campaign_name,
            campaign_type=campaign_type,
            status=status,
            start_date=start_date,
            end_date=end_date,
            budget=budget,
            revenue_generated=revenue_generated,
        )

        return self.repository.create(campaign)

    def delete_campaign(self, campaign_id: int):
        campaign = self.get_campaign(campaign_id)

        self.repository.delete(campaign)

        return {"message": "Campaign deleted successfully"}