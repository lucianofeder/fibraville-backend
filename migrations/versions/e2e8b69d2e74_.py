"""empty message

Revision ID: e2e8b69d2e74
Revises: b73454f973f1
Create Date: 2021-08-16 19:17:23.201206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e8b69d2e74'
down_revision = 'b73454f973f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atendimento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('descricao', sa.String(length=511), nullable=True),
    sa.Column('setor', sa.String(length=50), nullable=True),
    sa.Column('usuario_cpf', sa.String(length=11), nullable=True),
    sa.Column('usuario_telefone', sa.String(length=50), nullable=True),
    sa.Column('atendente_id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['atendente_id'], ['usuario.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('atendimento')
    # ### end Alembic commands ###