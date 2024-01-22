"""Create URLs Table

Revision ID: fa1a5879156f
Revises: 
Create Date: 2024-01-22 20:50:34.228055

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "fa1a5879156f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("origin", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("code"),
    )


def downgrade() -> None:
    op.drop_table("urls")
