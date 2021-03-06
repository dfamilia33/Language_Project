"""empty message

Revision ID: 5939923d6cc7
Revises: ead1f573cd09
Create Date: 2019-06-16 16:39:51.002688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5939923d6cc7'
down_revision = 'ead1f573cd09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'country', 'post', ['user_id'], ['id'])
    op.drop_column('post', 'countries')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('countries', sa.VARCHAR(length=100), nullable=True))
    op.drop_constraint(None, 'country', type_='foreignkey')
    # ### end Alembic commands ###
