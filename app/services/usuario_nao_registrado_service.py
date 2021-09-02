from app.models.usuario_nao_registrado_model import UsuarioNaoRegistradoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

def get_all() -> list[UsuarioNaoRegistradoModel]:
    data_list: list[UsuarioNaoRegistradoModel] = UsuarioNaoRegistradoModel.query.all()
    return [usuario for usuario in data_list]


def get_usuario_by_telefone(data):
    usuario: UsuarioNaoRegistradoModel = UsuarioNaoRegistradoModel.query.filter_by(telefone=data["telefone"]).first()
    if usuario:
        return usuario
    return None


def create_usuario() -> UsuarioNaoRegistradoModel:
    parser = reqparse.RequestParser()

    parser.add_argument("nome", type=str, required=True)
    parser.add_argument("telefone", type=str, required=True)
    parser.add_argument("e_comercial", type=bool, required=False)
    parser.add_argument("cep", type=str, required=False)
    parser.add_argument("rua", type=str, required=False)
    parser.add_argument("numero", type=str, required=False)
    parser.add_argument("complemento", type=str, required=False)
    parser.add_argument("bairro", type=str, required=False)
    parser.add_argument("cidade", type=str, required=False)
    parser.add_argument("estado", type=str, required=False)

    data = parser.parse_args(strict=True)

    new_usuario = get_usuario_by_telefone(data)

    if new_usuario:
        return jsonify(new_usuario), HTTPStatus.CONFLICT
    
    new_usuario: UsuarioNaoRegistradoModel = UsuarioNaoRegistradoModel(**data)
    new_usuario.save()

    return jsonify(new_usuario), HTTPStatus.CREATED