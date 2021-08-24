from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import jsonify

from app.services.usuario_endereco_service import UsuarioEnderecoService


class UsuarioEnderecoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = UsuarioEnderecoService.get_all()
        return response


class UsuarioEnderecoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, endereco_id):
        response, response.status_code = UsuarioEnderecoService.get_by_id(endereco_id)
        return response
    

    # @jwt_required()
    def patch(self, endereco_id):
        response, response.status_code = UsuarioEnderecoService.update(endereco_id)
        return response

    
    # @jwt_required()
    def delete(self, endereco_id):
        response, response.status_code = UsuarioEnderecoService.delete(endereco_id)
        return response


class UsuarioEnderecoByUserResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        response, response.status_code = UsuarioEnderecoService.get_by_user_id(usuario_id)
        return response

    # @jwt_required()
    def post(self, usuario_id):
        response, response.status_code = UsuarioEnderecoService.create(usuario_id)
        return response
