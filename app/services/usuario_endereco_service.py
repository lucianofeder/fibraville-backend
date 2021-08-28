from app.models.usuario_endereco_model import UsuarioEnderecoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.exc import DuplicatedData

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

        parser.add_argument("e_comercial", type=bool, store_missing=False)
        parser.add_argument("cep", type=str, store_missing=False)
        parser.add_argument("rua", type=str, store_missing=False)
        parser.add_argument("numero", type=str, store_missing=False)
        parser.add_argument("complemento", type=str, store_missing=False)
        parser.add_argument("bairro", type=str, store_missing=False)
        parser.add_argument("cidade", type=str, store_missing=False)
        parser.add_argument("estado", type=str, store_missing=False)
        parser.add_argument("referencia", type=str, store_missing=False)
        parser.add_argument("contato", type=str, store_missing=False)
        parser.add_argument("wireless_login", type=str, store_missing=False)
        parser.add_argument("wireless_senha", type=str, store_missing=False)
        parser.add_argument("onu_login", type=str, store_missing=False)
        parser.add_argument("onu_senha", type=str, store_missing=False)
        parser.add_argument("contrato_usuario_id", type=int, store_missing=False)

        data = parser.parse_args(strict=True)

        endereco_atual = UsuarioEnderecoModel.query.get(endereco_id)
        for key, value in data.items():
            setattr(endereco_atual, key, value)

        endereco_atual.save()
        return jsonify(endereco_atual), HTTPStatus.OK

    
    @staticmethod
    def delete(endereco_id) -> None:
        endereco = UsuarioEnderecoModel.query.get(endereco_id)
        if endereco:
            endereco.delete()
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_user_id(usuario_id):
        usuario_endereco = UsuarioEnderecoModel.query.filter_by(usuario_id=usuario_id)
        if usuario_endereco:
            return jsonify({"usuario_id": usuario_id, "enderecos": list(usuario_endereco)}), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def check_address(cep, numero, rua):
        endereco = UsuarioEnderecoModel.query.filter_by(cep=cep, numero=numero, rua=rua).first()
        if endereco:
            return True
        return False


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

        if UsuarioEnderecoService.check_address(cep=data.cep, numero=data.numero, rua=data.rua):
            raise DuplicatedData('Endereco')

        new_usuario_endereco: UsuarioEnderecoModel = UsuarioEnderecoModel(**data, usuario_id=usuario_id)
        new_usuario_endereco.save()

        return jsonify(new_usuario_endereco), HTTPStatus.CREATED

