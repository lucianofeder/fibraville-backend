from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.fornecedor_endereco_service import FornecedorEnderecoService


class FornecedorEnderecoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = FornecedorEnderecoService.get_all()
        return response


    def post(self):
        response, response.status_code = FornecedorEnderecoService.create()
        return response


class FornecedorEnderecoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, endereco_id):
        response, response.status_code = FornecedorEnderecoService.get_by_id(endereco_id)
        return response
    

    # @jwt_required()
    def patch(self, endereco_id):
        try:
            response, response.status_code = FornecedorEnderecoService.update(endereco_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, endereco_id):
        response, response.status_code = FornecedorEnderecoService.delete(endereco_id)
        return response


class FornecedorEnderecoByFornecedorResource(Resource):
    def get(self, fornecedor_id):
        try:
            response, response.status_code = FornecedorEnderecoService.get_by_fornecedor_id(fornecedor_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND