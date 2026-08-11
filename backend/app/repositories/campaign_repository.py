from sqlalchemy.orm import Session

from backend.app.models.campaign import Campaign


class CampaignRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Campaign).all()

    def get_by_id(self, campaign_id: int):
        return (
            self.db.query(Campaign)
            .filter(Campaign.id == campaign_id)
            .first()
        )

    def get_by_campaign_id(self, campaign_id: str):
        return (
            self.db.query(Campaign)
            .filter(Campaign.campaign_id == campaign_id)
            .first()
        )

    def get_by_project_id(self, project_id: int):
        return (
            self.db.query(Campaign)
            .filter(Campaign.project_id == project_id)
            .all()
        )

    def create(self, campaign: Campaign):
        self.db.add(campaign)
        self.db.commit()
        self.db.refresh(campaign)

        return campaign

    def update(self, campaign: Campaign):
        self.db.commit()
        self.db.refresh(campaign)

        return campaign

    def delete(self, campaign: Campaign):
        self.db.delete(campaign)
        self.db.commit()

        return True