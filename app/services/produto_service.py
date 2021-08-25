from app.models.produto_model import ProdutoModel
from app.models.fornecedor_model import FornecedorModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class ProdutoService:

    @staticmethod
    def get_all():
        produtos_list = ProdutoModel.query.all()
        return jsonify(produtos_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(produto_id) -> ProdutoModel:
        produto = ProdutoModel.query.get(produto_id)
        if produto:
            return jsonify(produto), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> ProdutoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("modelo", type=str, required=True)
        parser.add_argument("marca", type=str, required=True)
        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("estoque", type=float)
        parser.add_argument("velocidade", type=float)

        data = parser.parse_args(strict=True)

        new_produto: ProdutoModel = ProdutoModel(**data)
        new_produto.save()

        return new_produto


    @staticmethod
    def update(produto_id) -> ProdutoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("modelo", type=str)
        parser.add_argument("marca", type=str)
        parser.add_argument("valor", type=float)
        parser.add_argument("estoque", type=float)
        parser.add_argument("velocidade", type=float)

        data = parser.parse_args(strict=True)

        produto = ProdutoModel.query.get(produto_id)
        for key, value in data.items():
            setattr(produto, key, value)
        
        produto.save()
        return produto

    
    @staticmethod
    def delete(produto_id) -> None:
        produto = ProdutoModel.query.get(produto_id)
        if produto:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def get_by_fornecedor(fornecedor_id) -> ProdutoModel:

        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if fornecedor:
            raise DataNotFound('Fornecedor')        
        return jsonify(fornecedor.produtos_list), HTTPStatus.OK
