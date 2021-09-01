from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.produto_service import ProdutoService


class ProdutoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(ProdutoService.get_all())

    def post(self):
        try:
            return make_response(ProdutoService.create())
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class ProdutoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, produto_id):
        return make_response(ProdutoService.get_by_id(produto_id))
    

    # @jwt_required()
    def patch(self, produto_id):
        return make_response(ProdutoService.update(produto_id))

    
    # @jwt_required()
    def delete(self, produto_id):
        return make_response(ProdutoService.delete(produto_id))


class ProdutoByFornecedorResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        try:
            return make_response(ProdutoService.get_by_fornecedor(fornecedor_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
