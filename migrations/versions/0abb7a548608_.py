"""empty message

Revision ID: 0abb7a548608
Revises: 12b3e3d7883c
Create Date: 2019-06-16 18:12:54.727395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0abb7a548608'
down_revision = '12b3e3d7883c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country', sa.Column('approved', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###
