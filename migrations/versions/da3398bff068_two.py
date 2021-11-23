"""two

Revision ID: da3398bff068
Revises: 6c7e97a3aa8a
Create Date: 2021-11-23 23:17:58.384931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da3398bff068'
down_revision = '6c7e97a3aa8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file_base', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_base', sa.Column('test', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###