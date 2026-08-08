from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    industry: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    headquarters: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    ceo: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # One Company -> Many Departments
    departments: Mapped[list["Department"]] = relationship(
        "Department",
        back_populates="company",
        cascade="all, delete-orphan",
    )