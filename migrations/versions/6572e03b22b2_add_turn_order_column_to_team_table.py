"""add turn order column to team table

Revision ID: 6572e03b22b2
Revises: 4d2adc0ff9ab
Create Date: 2020-03-22 01:56:57.702487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6572e03b22b2'
down_revision = '4d2adc0ff9ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('turn_order', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'turn', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'turn', type_='unique')
    op.drop_column('team', 'turn_order')
    # ### end Alembic commands ###
