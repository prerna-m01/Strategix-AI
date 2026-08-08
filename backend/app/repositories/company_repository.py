from sqlalchemy.orm import Session

from backend.app.models.company import Company


class CompanyRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Company).all()

    def get_by_id(self, company_id: int):
        return (
            self.db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(Company)
            .filter(Company.name.ilike(name))
            .first()
        )

    def create(self, company: Company):
        self.db.add(company)
        self.db.commit()
        self.db.refresh(company)

        return company

    def update(self, company: Company):
        self.db.commit()
        self.db.refresh(company)

        return company

    def delete(self, company: Company):
        self.db.delete(company)
        self.db.commit()

        return True