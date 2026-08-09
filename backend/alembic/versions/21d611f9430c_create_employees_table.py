"""create employees table

Revision ID: 21d611f9430c
Revises: e129894ff7d3
Create Date: 2026-08-08 22:08:18.420731

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "21d611f9430c"
down_revision: Union[str, Sequence[str], None] = "e129894ff7d3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "employees",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("employee_id", sa.String(length=50), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("department_id", sa.Integer(), nullable=False),
        sa.Column("job_title", sa.String(length=255), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=False),
        sa.Column("employment_type", sa.String(length=50), nullable=False),
        sa.Column("hire_date", sa.Date(), nullable=False),
        sa.Column("annual_salary", sa.Numeric(precision=12, scale=2), nullable=False),
        sa.ForeignKeyConstraint(
            ["department_id"],
            ["departments.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_employees_department_id"),
        "employees",
        ["department_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_employees_email"),
        "employees",
        ["email"],
        unique=True,
    )

    op.create_index(
        op.f("ix_employees_employee_id"),
        "employees",
        ["employee_id"],
        unique=True,
    )

    op.create_index(
        op.f("ix_employees_id"),
        "employees",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_employees_id"),
        table_name="employees",
    )

    op.drop_index(
        op.f("ix_employees_employee_id"),
        table_name="employees",
    )

    op.drop_index(
        op.f("ix_employees_email"),
        table_name="employees",
    )

    op.drop_index(
        op.f("ix_employees_department_id"),
        table_name="employees",
    )

    op.drop_table("employees")