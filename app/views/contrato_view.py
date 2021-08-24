from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.contrato_service import ContratoService


class ContratoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = ContratoService.get_all()
        return response

    def post(self):
        try:
            response, response.status_code = ContratoService.create()
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class ContratoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, contrato_id):
        response, response.status_code = ContratoService.get_by_id(contrato_id)
        return response
    

    # @jwt_required()
    def patch(self, contrato_id):
        response, response.status_code = ContratoService.update(contrato_id)
        return response

    
    # @jwt_required()
    def delete(self, contrato_id):
        response, response.status_code = ContratoService.delete(contrato_id)
        return response

