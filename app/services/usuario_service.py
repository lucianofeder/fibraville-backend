from datetime import datetime
from app.models.usuario_model import UsuarioModel
from app.models.usuario_permissao_model import UsuarioPermissaoModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token
from http import HTTPStatus


class UsuarioService:

    @staticmethod
    def get_all():
        usuarios_list = UsuarioModel.query.all()
        return jsonify(usuarios_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(usuario_id) -> UsuarioModel:
        usuario = UsuarioModel.query.get(usuario_id)
        if usuario:
            return jsonify(usuario), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> UsuarioModel:
        parser = reqparse.RequestParser()

        parser.add_argument("nome", type=str, required=True)
        parser.add_argument("sobrenome", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
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
        usuario_permissao = data.pop('usuario_permissao')

        new_permissao = UsuarioPermissaoModel(**usuario_permissao)
        new_permissao.save()

        data.usuario_permissao_id = new_permissao.id

        new_usuario: UsuarioModel = UsuarioModel(**data)
        new_usuario.save()

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
    def delete(usuario_id) -> None:
        usuario = UsuarioModel.query.get(usuario_id)
        if usuario:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND

    
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

