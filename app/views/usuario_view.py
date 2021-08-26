from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.usuario_service import UsuarioService


class UsuarioResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = UsuarioService.get_all()
        return response

    def post(self):
        response, response.status_code = UsuarioService.create()
        return response


class UsuarioRetrieveResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        response, response.status_code = UsuarioService.get_by_id(usuario_id)
        return response
    

    # @jwt_required()
    def patch(self, usuario_id):
        try:
            response, response.status_code = UsuarioService.update(usuario_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


    
    # @jwt_required()
    def delete(self, usuario_id):
        response, response.status_code = UsuarioService.delete(usuario_id)
        return response


class UsuarioLoginResource(Resource):

    def post(self):
        try:
            response, response.status_code = UsuarioService.login()
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
