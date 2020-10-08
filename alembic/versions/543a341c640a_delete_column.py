"""delete column

Revision ID: 543a341c640a
Revises: b43cd0cc0eb9
Create Date: 2020-10-08 10:38:22.405421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543a341c640a'
down_revision = 'b43cd0cc0eb9'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('task', 'done')


def downgrade():
    op.add_column('task', sa.Column('done', sa.String(50)))
