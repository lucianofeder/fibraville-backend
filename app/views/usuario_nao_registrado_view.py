from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.usuario_nao_registrado_service import get_all, create_usuario


class UsuarioNaoRegistradoResource(Resource):
    # @jwt_required()
    def get(self):
        return get_all()
    

    # @jwt_required()
    def post(self):
        return create_usuario()