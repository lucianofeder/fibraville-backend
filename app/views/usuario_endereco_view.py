from app.exc import DuplicatedData
from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import jsonify, make_response

from app.services.usuario_endereco_service import UsuarioEnderecoService


class UsuarioEnderecoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(UsuarioEnderecoService.get_all())


class UsuarioEnderecoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, endereco_id):
        return make_response(UsuarioEnderecoService.get_by_id(endereco_id))

    
    # @jwt_required()
    def patch(self, endereco_id):
        try:
            return make_response(UsuarioEnderecoService.update(endereco_id))
        except DuplicatedData as e:
            return e.message, HTTPStatus.BAD_REQUEST
    
    # @jwt_required()
    def delete(self, endereco_id):
        return make_response(UsuarioEnderecoService.delete(endereco_id))


class UsuarioEnderecoByUserResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        return make_response(UsuarioEnderecoService.get_by_user_id(usuario_id))


    # @jwt_required()
    def post(self, usuario_id):
        try:
            return make_response(UsuarioEnderecoService.create(usuario_id))
        except DuplicatedData as e:
            return e.message, HTTPStatus.BAD_REQUEST