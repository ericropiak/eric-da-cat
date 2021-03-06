"""add player id to turn table

Revision ID: 043244e70763
Revises: 70ce1137b033
Create Date: 2020-03-22 03:28:46.159575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043244e70763'
down_revision = '70ce1137b033'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guessed_word',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('round_id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['round_id'], ['round.id'], ),
    sa.ForeignKeyConstraint(['word_id'], ['salad_bowl_word.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'round_id', 'word_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guessed_word')
    # ### end Alembic commands ###
