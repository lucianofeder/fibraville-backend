from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import json, jsonify, request

from app.services.usuario_permissao_service import UsuarioPermissaoService


class UsuarioPermissaoResource(Resource):
    # @jwt_required()
    def get(self):
        response = jsonify(UsuarioPermissaoService.get_all())
        response.status_code = HTTPStatus.OK
        return response
    

class UsuarioPermissaoRetrieveResource(Resource):
    # jwt_required()
    def get(self, usuario_id):
        response, response.status_code = UsuarioPermissaoService.get_by_user_id(usuario_id)
        return response
    
    # jwt_required() => Apenas usuarios administradores
    def patch(self, usuario_id):
        data = request.get_json()
        return jsonify(UsuarioPermissaoService.update(usuario_id=usuario_id, data=data)), HTTPStatus.OK
