from app.models.usuario_endereco_model import UsuarioEnderecoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class UsuarioEnderecoService:

    @staticmethod
    def get_all():
        enderecos = UsuarioEnderecoModel.query.all()
        return jsonify(enderecos), HTTPStatus.OK 

    @staticmethod
    def get_by_id(endereco_id) -> UsuarioEnderecoModel:
        usuario_endereco = UsuarioEnderecoModel.query.get(endereco_id)
        if usuario_endereco:
            return jsonify(usuario_endereco), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND

    @staticmethod
    def update(endereco_id) -> UsuarioEnderecoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("e_comercial", type=bool, default=False)
        parser.add_argument("cep", type=str, required=True)
        parser.add_argument("rua", type=str, required=True)
        parser.add_argument("numero", type=str, default='SN')
        parser.add_argument("complemento", type=str)
        parser.add_argument("bairro", type=str, required=True)
        parser.add_argument("cidade", type=str, required=True)
        parser.add_argument("estado", type=str, required=True)
        parser.add_argument("referencia", type=str)
        parser.add_argument("contato", type=str)
        parser.add_argument("wireless_login", type=str)
        parser.add_argument("wireless_senha", type=str)
        parser.add_argument("onu_login", type=str)
        parser.add_argument("onu_senha", type=str)
        parser.add_argument("contrato_usuario_id", type=int)

        data = parser.parse_args(strict=True)

        endereco_atual = UsuarioEnderecoModel.query.get(endereco_id)
        for key, value in data.items():
            setattr(endereco_atual, key, value)
        
        endereco_atual.save()
        return endereco_atual

    
    @staticmethod
    def delete(endereco_id) -> None:
        endereco = UsuarioEnderecoModel.query.get(endereco_id)
        if endereco:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_user_id(usuario_id):
        usuario_endereco = UsuarioEnderecoModel.query.filter(usuario_id=usuario_id)
        if usuario_endereco:
            return jsonify({"usuario_id": usuario_id, "enderecos": usuario_endereco}), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(usuario_id) -> UsuarioEnderecoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("e_comercial", type=bool, default=False)
        parser.add_argument("cep", type=str, required=True)
        parser.add_argument("rua", type=str, required=True)
        parser.add_argument("numero", type=str, default='SN')
        parser.add_argument("complemento", type=str)
        parser.add_argument("bairro", type=str, required=True)
        parser.add_argument("cidade", type=str, required=True)
        parser.add_argument("estado", type=str, required=True)
        parser.add_argument("referencia", type=str)
        parser.add_argument("contato", type=str)
        parser.add_argument("wireless_login", type=str)
        parser.add_argument("wireless_senha", type=str)
        parser.add_argument("onu_login", type=str)
        parser.add_argument("onu_senha", type=str)
        parser.add_argument("contrato_usuario_id", type=int)

        data = parser.parse_args(strict=True)

        new_usuario_endereco: UsuarioEnderecoModel = UsuarioEnderecoModel(**data, usuario_id=usuario_id)
        new_usuario_endereco.save()

        return new_usuario_endereco

