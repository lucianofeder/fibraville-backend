from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.atendimento_service import AtendimentoService


class AtendimentoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = AtendimentoService.get_all()
        return response

    def post(self):
        try:
            response, response.status_code = AtendimentoService.create()
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class AtendimentoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, atendimento_id):
        response, response.status_code = AtendimentoService.get_by_id(atendimento_id)
        return response
    

    # @jwt_required()
    def patch(self, atendimento_id):
        response, response.status_code = AtendimentoService.update(atendimento_id)
        return response

    
    # @jwt_required()
    def delete(self, atendimento_id):
        response, response.status_code = AtendimentoService.delete(atendimento_id)
        return response


class AtendimentoByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        try:
            response, response.status_code = AtendimentoService.get_by_usuario(usuario_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
