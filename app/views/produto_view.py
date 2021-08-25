from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.produto_service import ProdutoService


class ProdutoResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = ProdutoService.get_all()
        return response

    def post(self):
        try:
            response, response.status_code = ProdutoService.create()
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class ProdutoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, produto_id):
        response, response.status_code = ProdutoService.get_by_id(produto_id)
        return response
    

    # @jwt_required()
    def patch(self, produto_id):
        response, response.status_code = ProdutoService.update(produto_id)
        return response

    
    # @jwt_required()
    def delete(self, produto_id):
        response, response.status_code = ProdutoService.delete(produto_id)
        return response


class ProdutoByFornecedorResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        try:
            response, response.status_code = ProdutoService.get_by_usuario(usuario_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
