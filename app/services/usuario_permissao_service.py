from app.models.usuario_permissao_model import UsuarioPermissaoModel
from app.models.usuario_model import UsuarioModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.exc import DataNotFound
from app.services.helper import BaseServices


class UsuarioPermissaoService(BaseServices):
    model = UsuarioPermissaoModel


    @staticmethod
    def get_by_user_id(usuario_id):
        usuario_permissao = UsuarioModel.query.get(usuario_id).usuario_permissao
        if usuario_permissao:
            return jsonify(usuario_permissao), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(usuario, e_cliente=True, e_representante=False, e_comercial=False) -> UsuarioPermissaoModel:
        
        new_usuario_permissao: UsuarioPermissaoModel = UsuarioPermissaoModel(usuario=usuario, e_cliente=e_cliente, e_representante=e_representante, e_comercial=e_comercial)
        new_usuario_permissao.save()

        return new_usuario_permissao

    
    @staticmethod
    def update(usuario_id) -> UsuarioPermissaoModel:
        usuario = UsuarioModel.query.get(usuario_id)

        if not usuario:
            raise DataNotFound("Usuario")

        parser = reqparse.RequestParser()

        parser.add_argument("e_cliente", type=bool, store_missing=False)
        parser.add_argument("e_representante", type=bool, store_missing=False)
        parser.add_argument("e_comercial", type=bool, store_missing=False)
        
        data = parser.parse_args()

        permissao_atual = UsuarioPermissaoModel.query.get(usuario.usuario_permissao_id)

        for key, value in data.items():
            setattr(permissao_atual, key, value)
        
        permissao_atual.save()
        return jsonify(permissao_atual), HTTPStatus.OK

