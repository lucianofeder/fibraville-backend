from http import HTTPStatus

from flask.helpers import make_response
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.fornecedor_endereco_service import FornecedorEnderecoService


class FornecedorEnderecoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(FornecedorEnderecoService.get_all())



class FornecedorEnderecoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, endereco_id):
        return make_response(FornecedorEnderecoService.get_by_id(endereco_id))
    

    # @jwt_required()
    def patch(self, endereco_id):
        try:
            return make_response(FornecedorEnderecoService.update(endereco_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, endereco_id):
        return make_response(FornecedorEnderecoService.delete(endereco_id))


class FornecedorEnderecoByFornecedorResource(Resource):
    def get(self, fornecedor_id):
        try:
            return make_response(FornecedorEnderecoService.get_by_fornecedor_id(fornecedor_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
    

    def post(self, fornecedor_id):
        try:
            return make_response(FornecedorEnderecoService.create(fornecedor_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND