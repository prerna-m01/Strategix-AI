from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    industry = Column(String(100), nullable=False)

    headquarters = Column(String(150), nullable=False)

    ceo = Column(String(150), nullable=False)

    departments = relationship(
        "Department",
        back_populates="company",
        cascade="all, delete-orphan",
    )