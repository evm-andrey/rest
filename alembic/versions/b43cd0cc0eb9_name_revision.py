"""name revision

Revision ID: b43cd0cc0eb9
Revises: 
Create Date: 2020-10-08 10:05:23.183615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b43cd0cc0eb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('task', sa.Column('last_transaction_date', sa.String(50)))


def downgrade():
    op.drop_column('task', 'last_transaction_date')
