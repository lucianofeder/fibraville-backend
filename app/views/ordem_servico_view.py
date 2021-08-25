from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.ordem_servico_service import OrdemServicoService


class OrdemServicoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = OrdemServicoService.get_all()
        return response

    def post(self):
        try:
            response, response.status_code = OrdemServicoService.create()
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class OrdemServicoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, os_id):
        response, response.status_code = OrdemServicoService.get_by_id(os_id)
        return response
    

    # @jwt_required()
    def patch(self, os_id):
        response, response.status_code = OrdemServicoService.update(os_id)
        return response

    
    # @jwt_required()
    def delete(self, os_id):
        response, response.status_code = OrdemServicoService.delete(os_id)
        return response


class OrdemServicoByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        try:
            response, response.status_code = OrdemServicoService.get_by_usuario(usuario_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
