from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.ordem_servico_service import OrdemServicoService


class OrdemServicoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(OrdemServicoService.get_all())

    def post(self):
        try:
            return make_response(OrdemServicoService.create())
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class OrdemServicoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, os_id):
        return make_response(OrdemServicoService.get_by_id(os_id))
    

    # @jwt_required()
    def patch(self, os_id):
        return make_response(OrdemServicoService.update(os_id))

    
    # @jwt_required()
    def delete(self, os_id):
        return make_response(OrdemServicoService.delete(os_id))


class OrdemServicoByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        try:
            return make_response(OrdemServicoService.get_by_usuario(usuario_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
