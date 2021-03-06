"""Add deleted flag

Revision ID: 109770ba0d9b
Revises: ba823205d87f
Create Date: 2020-05-04 22:43:38.881201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "109770ba0d9b"
down_revision = "ba823205d87f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column("deleted", sa.Boolean(), server_default="FALSE", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "deleted")
    # ### end Alembic commands ###
