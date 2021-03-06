"""empty message

Revision ID: 089ef69d65f3
Revises: 6cfc9daeecbe
Create Date: 2020-12-08 10:44:29.695008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '089ef69d65f3'
down_revision = '6cfc9daeecbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('image_file', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'image_file')
    # ### end Alembic commands ###
