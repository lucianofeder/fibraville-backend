from click import argument, echo, option
from flask.cli import AppGroup
from flask import Flask

import secrets

from app.models.usuario_model import UsuarioModel
from app.models.usuario_permissao_model import UsuarioPermissaoModel


def update(cpf, email, admin: bool=False):
    usuario = None
    usuario_email = None
    usuario_cpf = None
    if cpf:
        usuario_cpf = UsuarioModel.query.filter_by(cpf=cpf).first()
    if email:
        usuario_email = UsuarioModel.query.filter_by(email=email).first()
    if usuario_cpf and usuario_email:
        if usuario_cpf != usuario_email:
            echo(f'Informacoes inconsistentes cpf:{cpf} nao pertence ao mesmo usuario de email:{email}')
            return None
    if not usuario_cpf and not usuario_email:
        echo(f'Usuario nao encontrado')
        return None

    usuario = usuario_cpf if usuario_cpf else usuario_email
    usuario_permissao = UsuarioPermissaoModel.query.filter_by(e_cliente=usuario.usuario_permissao.e_cliente, e_representante=usuario.usuario_permissao.e_representante, e_funcionario=usuario.usuario_permissao.e_funcionario, e_super_usuario=admin).first()
    if not usuario_permissao:
        usuario_permissao: UsuarioPermissaoModel = UsuarioPermissaoModel(e_cliente=usuario.usuario_permissao.e_cliente, e_representante=usuario.usuario_permissao.e_representante, e_funcionario=usuario.usuario_permissao.e_funcionario, e_super_usuario=admin)
        usuario_permissao.save()
    
    usuario.usuario_permissao_id = usuario_permissao.id
    usuario.save()

    return usuario


def cli_admin(app: Flask):
    cli_admin_group = AppGroup('admin')

    @cli_admin_group.command('create')
    @argument('nome')
    @argument('sobrenome')
    @argument('cpf')
    @argument('email')
    def cli_admin_create(nome: str, sobrenome: str, cpf:str='032teste', email: str='teste'):
        usuario_check = UsuarioModel.query.filter_by(cpf=cpf).first()
        echo(f'email: {email}, cpf:{cpf}')
        if usuario_check:
            echo('')
            echo(f'ERROR: Usuario com cpf {cpf} ja cadastrado na base de dados')
            echo(f'Utilizar flask admin upgrade --cpf={cpf}')
            return None
        
        usuario_check = UsuarioModel.query.filter_by(email=email).first()
        if usuario_check:
            echo('')
            echo(f'ERROR: Usuario com email {email} ja cadastrado na base de dados')
            echo(f'Utilizar flask admin upgrade --email={email}')
            return None

        usuario_permissao = UsuarioPermissaoModel.query.filter_by(e_cliente=False, e_representante=False, e_funcionario=False, e_super_usuario=True).first()
        if not usuario_permissao:
            usuario_permissao: UsuarioPermissaoModel = UsuarioPermissaoModel(e_cliente=False, e_representante=False, e_funcionario=False, e_super_usuario=True)
            usuario_permissao.save()
        
        password = secrets.token_hex(12)

        new_admin = UsuarioModel(nome=nome, sobrenome=sobrenome, cpf=cpf, email=email, usuario_permissao=usuario_permissao, password=password)
        new_admin.save()
        echo('Usuario criado com sucesso')
        echo(f'cpf: {cpf}')
        echo(f'password: {password}')
    

    @cli_admin_group.command('upgrade')
    @option('--cpf', default=None)
    @option('--email', default=None)
    def cli_admin_upgrade(cpf: str, email: str):
        usuario = update(cpf, email, admin=True)
        if usuario:
            echo(f'Upgrade no(a) {usuario.nome} realizado com sucesso')
    

    @cli_admin_group.command('downgrade')
    @option('--cpf', default=None)
    @option('--email', default=None)
    def cli_admin_downgrade(cpf: str, email: str):
        usuario = update(cpf, email, admin=False)
        if usuario:
            echo(f'Downgrade no(a) {usuario.nome} realizado com sucesso')

    app.cli.add_command(cli_admin_group)



def init_app(app: Flask):
    cli_admin(app)