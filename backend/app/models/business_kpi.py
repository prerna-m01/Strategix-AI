from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.database.base import Base


class BusinessKPI(Base):
    __tablename__ = "business_kpis"

    id = Column(Integer, primary_key=True, index=True)

    metric_name = Column(String(100), nullable=False)

    metric_value = Column(Float, nullable=False)

    unit = Column(String(30), nullable=False)

    year = Column(Integer, nullable=False)

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False,
    )

    department = relationship(
        "Department",
        back_populates="kpis",
    )