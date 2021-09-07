from http import HTTPStatus
from app.exc import DataNotFound, DuplicatedData
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response
from flask_mail import Message

from app.services.usuario_service import UsuarioService
from app.configs import mail


class UsuarioResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(UsuarioService.get_all())


    def post(self):
        try:
            return make_response(UsuarioService.create())
        except DuplicatedData as e:
            return e.message, HTTPStatus.BAD_REQUEST


class UsuarioRetrieveResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        return make_response(UsuarioService.get_by_id(usuario_id))
    

    # @jwt_required()
    def patch(self, usuario_id):
        try:
            return make_response(UsuarioService.update(usuario_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, usuario_id):
        return make_response(UsuarioService.delete(usuario_id))


class UsuarioLoginResource(Resource):

    def post(self):
        try:
            return make_response(UsuarioService.login())
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
