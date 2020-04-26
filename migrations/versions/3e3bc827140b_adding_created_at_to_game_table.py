"""adding created_at to game table

Revision ID: 3e3bc827140b
Revises: 3efe8111ce26
Create Date: 2020-04-26 17:03:01.893601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e3bc827140b'
down_revision = '3efe8111ce26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.execute('UPDATE game SET created_at = started_at;')
    op.alter_column('game', 'created_at', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('game', 'created_at')
    # ### end Alembic commands ###
