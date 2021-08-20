from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import jsonify

from app.services.usuario_nao_registrado_service import get_all, create_usuario


class UsuarioNaoRegistradoResource(Resource):
    # @jwt_required()
    def get(self):
        response = jsonify(get_all())
        response.status_code = HTTPStatus.OK
        return response
    

    # @jwt_required()
    def post(self):
        data, status = create_usuario()
        response = data
        response.status_code = status
        return response