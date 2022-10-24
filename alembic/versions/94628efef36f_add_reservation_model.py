"""add reservation model

Revision ID: 94628efef36f
Revises: 1fee3f605dfa
Create Date: 2022-10-24 22:39:23.216445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94628efef36f'
down_revision = '1fee3f605dfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###