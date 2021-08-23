from app.models.usuario_permissao_model import UsuarioPermissaoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class UsuarioPermissaoService:

    @staticmethod
    def get_all() -> list[UsuarioPermissaoModel]:
        data_list: list[UsuarioPermissaoModel] = UsuarioPermissaoModel.query.all()
        return [usuario_permissao for usuario_permissao in data_list]


    @staticmethod
    def get_by_id(id) -> UsuarioPermissaoModel:
        usuario_permissao = UsuarioPermissaoModel.query.get(id)
        if usuario_permissao:
            return jsonify(usuario_permissao), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_user_id(usuario_id):
        usuario_permissao = UsuarioPermissaoModel.query.filter(usuario_id=usuario_id).first()
        if usuario_permissao:
            return jsonify(usuario_permissao), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND



    @staticmethod
    def create(usuario, e_cliente=True, e_representante=False, e_comercial=False) -> UsuarioPermissaoModel:
        
        new_usuario_permissao: UsuarioPermissaoModel = UsuarioPermissaoModel(usuario=usuario, e_cliente=e_cliente, e_representante=e_representante, e_comercial=e_comercial)
        new_usuario_permissao.save()

        return new_usuario_permissao

    
    @staticmethod
    def update(usuario_id, data) -> UsuarioPermissaoModel:
        #TRATAR ERRO DE USUARIO NAO ENCONTRADO
        permissao_atual = UsuarioPermissaoModel.query.filter(usuario_id=usuario_id).first()
        for key, value in data.items():
            setattr(permissao_atual, key, value)
        
        permissao_atual.save()
        return permissao_atual

