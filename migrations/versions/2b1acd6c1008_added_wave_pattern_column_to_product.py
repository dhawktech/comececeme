"""added wave_pattern column to Product

Revision ID: 2b1acd6c1008
Revises: 5b6f8814984f
Create Date: 2020-08-26 08:15:25.089838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b1acd6c1008'
down_revision = '5b6f8814984f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('wave_pattern', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'wave_pattern')
    # ### end Alembic commands ###
