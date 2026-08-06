from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    description = Column(String(500))

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
    )

    company = relationship(
        "Company",
        back_populates="departments",
    )

    kpis = relationship(
        "BusinessKPI",
        back_populates="department",
        cascade="all, delete-orphan",
    )