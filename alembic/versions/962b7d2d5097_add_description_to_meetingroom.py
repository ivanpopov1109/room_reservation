"""Add description to MeetingRoom

Revision ID: 962b7d2d5097
Revises: 764fb8329781
Create Date: 2022-10-14 08:53:17.283416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '962b7d2d5097'
down_revision = '764fb8329781'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###