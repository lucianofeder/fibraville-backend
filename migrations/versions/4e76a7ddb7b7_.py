"""empty message

Revision ID: 4e76a7ddb7b7
Revises: d6d71d99eaea
Create Date: 2021-08-12 20:56:10.137668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e76a7ddb7b7'
down_revision = 'd6d71d99eaea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contrato',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('duracao_meses', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contrato')
    # ### end Alembic commands ###