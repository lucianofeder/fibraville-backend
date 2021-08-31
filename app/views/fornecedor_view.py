from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.fornecedor_service import FornecedorService


class FornecedorResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(FornecedorService.get_all())


    def post(self):
        return make_response(FornecedorService.create())


class FornecedorRetrieveResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        return make_response(FornecedorService.get_by_id(fornecedor_id))
    

    # @jwt_required()
    def patch(self, fornecedor_id):
        try:
            return make_response(FornecedorService.update(fornecedor_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, fornecedor_id):
        return make_response(FornecedorService.delete(fornecedor_id))

