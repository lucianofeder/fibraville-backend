"""empty message

Revision ID: b73454f973f1
Revises: 3312007d7c74
Create Date: 2021-08-15 22:37:18.233115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73454f973f1'
down_revision = '3312007d7c74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario_nao_registrado', sa.Column('e_comercial', sa.Boolean(), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('cep', sa.String(length=8), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('rua', sa.String(length=150), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('numero', sa.Integer(), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('complemento', sa.String(length=255), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('bairro', sa.String(length=150), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('cidade', sa.String(length=150), nullable=True))
    op.add_column('usuario_nao_registrado', sa.Column('estado', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario_nao_registrado', 'estado')
    op.drop_column('usuario_nao_registrado', 'cidade')
    op.drop_column('usuario_nao_registrado', 'bairro')
    op.drop_column('usuario_nao_registrado', 'complemento')
    op.drop_column('usuario_nao_registrado', 'numero')
    op.drop_column('usuario_nao_registrado', 'rua')
    op.drop_column('usuario_nao_registrado', 'cep')
    op.drop_column('usuario_nao_registrado', 'e_comercial')
    # ### end Alembic commands ###