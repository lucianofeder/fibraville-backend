from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.atendimento_service import AtendimentoService


class AtendimentoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(AtendimentoService.get_all())

    def post(self):
        try:
            return make_response(AtendimentoService.create())
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class AtendimentoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, atendimento_id):
        return make_response(AtendimentoService.get_by_id(atendimento_id))
    

    # @jwt_required()
    def patch(self, atendimento_id):
        try:
            return make_response(AtendimentoService.update(atendimento_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND  
        
    
    # @jwt_required()
    def delete(self, atendimento_id):
        return make_response(AtendimentoService.delete(atendimento_id))


class AtendimentoByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        try:
            return make_response(AtendimentoService.get_by_usuario(usuario_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
