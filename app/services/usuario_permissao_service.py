from app.models.usuario_permissao_model import UsuarioPermissaoModel
from app.models.usuario_model import UsuarioModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.exc import DataNotFound
from app.services.helper import BaseServices
import ipdb


class UsuarioPermissaoService(BaseServices):
    model = UsuarioPermissaoModel


    @staticmethod
    def get_by_user_id(usuario_id):
        usuario_permissao = UsuarioModel.query.get(usuario_id).usuario_permissao
        if usuario_permissao:
            return jsonify(usuario_permissao), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(e_cliente=True, e_representante=False, e_funcionario=False, e_super_usuario=False) -> UsuarioPermissaoModel:
        
        usuario_permissao = UsuarioPermissaoModel.query.filter_by(e_cliente=e_cliente, e_representante=e_representante, e_funcionario=e_funcionario, e_super_usuario=e_super_usuario).first()
        if usuario_permissao:
            return usuario_permissao

        new_usuario_permissao: UsuarioPermissaoModel = UsuarioPermissaoModel(e_cliente=e_cliente, e_representante=e_representante, e_funcionario=e_funcionario, e_super_usuario=e_super_usuario)
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

