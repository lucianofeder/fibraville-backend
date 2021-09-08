from app.services.usuario_permissao_service import UsuarioPermissaoService
from app.services.helper import BaseServices, EmailServices
from datetime import datetime
from app.models.usuario_model import UsuarioModel
from app.models.usuario_permissao_model import UsuarioPermissaoModel
from app.exc import DataNotFound
from flask_restful import reqparse, current_app
from flask import jsonify
from flask_jwt_extended import create_access_token
from http import HTTPStatus
from app.exc import DuplicatedData
import secrets
from threading import Thread


class UsuarioService(BaseServices):
    model = UsuarioModel


    @staticmethod
    def create() -> UsuarioModel:
        parser = reqparse.RequestParser()

        parser.add_argument("nome", type=str, required=True)
        parser.add_argument("sobrenome", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("data_nascimento", type=datetime)
        parser.add_argument("e_pessoa_fisica", type=bool, default=True)
        parser.add_argument("cpf", type=str)
        parser.add_argument("cnpj", type=str)
        parser.add_argument("mae_nome", type=str)
        parser.add_argument("pai_nome", type=str)
        parser.add_argument("observacao", type=str)
        parser.add_argument("usuario_permissao", type=dict, required=True)

        data = parser.parse_args(strict=True)
        data['password'] = secrets.token_hex(8)

        usuario_check = UsuarioModel.query.filter_by(cpf=data.cpf).first()
        if usuario_check:
            raise DuplicatedData('CPF')
        
        usuario_check = UsuarioModel.query.filter_by(email=data.email).first()
        if usuario_check:
            raise DuplicatedData('Email')

        usuario_permissao = data.pop('usuario_permissao')

        if 'e_super_usuario' in usuario_permissao:
            usuario_permissao.pop('e_super_usuario')
        new_permissao = UsuarioPermissaoService.create(**usuario_permissao)

        data.usuario_permissao_id = new_permissao.id

        new_usuario: UsuarioModel = UsuarioModel(**data)
        new_usuario.save()
        
        EmailServices.send_password(data['password'], new_usuario)

        # thread = Thread(target=EmailServices.send_password, kwargs={'password': data['password'], 'usuario': new_usuario})
        # thread.start()

        return jsonify(new_usuario), HTTPStatus.CREATED


    @staticmethod
    def update(usuario_id) -> UsuarioModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("nome", type=str, store_missing=False)
        parser.add_argument("sobrenome", type=str, store_missing=False)
        parser.add_argument("password", type=str, store_missing=False)
        parser.add_argument("email", type=str, store_missing=False)
        parser.add_argument("data_nascimento", type=datetime, store_missing=False)
        parser.add_argument("e_pessoa_fisica", type=bool, store_missing=False)
        parser.add_argument("cpf", type=str, store_missing=False)
        parser.add_argument("cnpj", type=str, store_missing=False)
        parser.add_argument("mae_nome", type=str, store_missing=False)
        parser.add_argument("pai_nome", type=str, store_missing=False)
        parser.add_argument("observacao", type=str, store_missing=False)

        data = parser.parse_args()
        usuario = UsuarioModel.query.get(usuario_id)
        if not usuario:
            raise DataNotFound('Usuario')
                
        for key, value in data.items():
            setattr(usuario, key, value)
        
        usuario.save()
        return jsonify(usuario), HTTPStatus.OK

    
    @staticmethod
    def login():
        parser = reqparse.RequestParser()

        parser.add_argument("cpf", type=str, required=True)
        parser.add_argument('password', type=str, required=True)

        data = parser.parse_args(strict=True)

        usuario: UsuarioModel = UsuarioModel.query.filter_by(cpf=data['cpf']).first()

        if not usuario:
            raise DataNotFound('Usuario')

        if usuario.check_password(data['password']):
            token = create_access_token(identity=usuario)
            usuario.ultimo_login = datetime.utcnow()
            usuario.save()  
            return {"usuario_id": usuario.id, "token": token}, HTTPStatus.ACCEPTED
        else:
            return {"mensagem": "Informacoes de login invalidas"}, HTTPStatus.UNAUTHORIZED

    @staticmethod
    def generate_temp_token():
        parser = reqparse.RequestParser()

        parser.add_argument("cpf", type=str, required=True)
        parser.add_argument("email", type=str, required=True)

        data = parser.parse_args()

        usuario = UsuarioModel.query.filter_by(cpf=data['cpf']).first()

        if not usuario or usuario.email != data['email']:
            return {"error": "Informacoes invalidas"}, HTTPStatus.BAD_REQUEST
        
        temp_token = secrets.token_hex(32)
        current_app.cache.set(f"{data['email']}_temp_token", temp_token)

        EmailServices.send_temp_token(temp_token, usuario)

        return {"message": "Link de recuperacao enviado para o email", "token": temp_token}, HTTPStatus.OK
    
    @staticmethod
    def new_password_from_temp_token(usuario_id):
        parser = reqparse.RequestParser()

        parser.add_argument("cpf", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        parser.add_argument("temp_token", type=str, required=True)

        data = parser.parse_args()
        
        usuario = UsuarioModel.query.get(usuario_id)
        temp_token = current_app.cache.get(f"{usuario.email}_temp_token")

        if usuario.cpf != data['cpf'] or temp_token != data['temp_token']:
            return {}, HTTPStatus.BAD_REQUEST
        
        usuario.password = data['password']
        usuario.save()

        return {"message": "Senha trocada com sucesso"}, HTTPStatus.ACCEPTED


        

        
