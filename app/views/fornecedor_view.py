from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.fornecedor_service import FornecedorService


class FornecedorResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = FornecedorService.get_all()
        return response


    def post(self):
        response, response.status_code = FornecedorService.create()
        return response


class FornecedorRetrieveResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        response, response.status_code = FornecedorService.get_by_id(fornecedor_id)
        return response
    

    # @jwt_required()
    def patch(self, fornecedor_id):
        try:
            response, response.status_code = FornecedorService.update(fornecedor_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, fornecedor_id):
        response, response.status_code = FornecedorService.delete(fornecedor_id)
        return response

