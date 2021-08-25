from app.exc import DataNotFound
from app.models.fornecedor_model import FornecedorModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class FornecedorService:

    @staticmethod
    def get_all():
        fornecedores_list = FornecedorModel.query.all()
        return jsonify(fornecedores_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(fornecedor_id) -> FornecedorModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if fornecedor:
            return jsonify(fornecedor), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> FornecedorModel:
        parser = reqparse.RequestParser()

        parser.add_argument("razao_social", type=str, required=True)
        parser.add_argument("nome_fantasia", type=str)
        parser.add_argument("cnpj", type=str, required=True)
        parser.add_argument("inscricao_estadual", type=str)
        parser.add_argument("contato", type=str)

        data = parser.parse_args(strict=True)

        new_fornecedor: FornecedorModel = FornecedorModel(**data)
        new_fornecedor.save()

        return new_fornecedor


    @staticmethod
    def update(fornecedor_id) -> FornecedorModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if not fornecedor:
            raise DataNotFound('Fornecedor')

        parser = reqparse.RequestParser()

        parser.add_argument("razao_social", type=str)
        parser.add_argument("nome_fantasia", type=str)
        parser.add_argument("cnpj", type=str)
        parser.add_argument("inscricao_estadual", type=str)
        parser.add_argument("contato", type=str)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(fornecedor, key, value)
        
        fornecedor.save()
        return fornecedor

    
    @staticmethod
    def delete(fornecedor_id) -> None:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if fornecedor:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND
