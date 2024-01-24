"""Create URLs Table

Revision ID: fa1a5879156f
Revises:
Create Date: 2024-01-22 20:50:34.228055

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "fa1a5879156f"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("origin", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("code"),
    )


def downgrade() -> None:
    op.drop_table("urls")
