"""empty message

Revision ID: 4b02e0ff73c8
Revises: e372d24aa34c
Create Date: 2021-09-07 14:55:13.347186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b02e0ff73c8'
down_revision = 'e372d24aa34c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario_permissao', sa.Column('e_super_usuario', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario_permissao', 'e_super_usuario')
    # ### end Alembic commands ###
