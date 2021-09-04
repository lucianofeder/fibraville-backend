from app.exc import DataNotFound
from app.models.fornecedor_model import FornecedorModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices


class FornecedorService(BaseServices):
    model = FornecedorModel


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

        return jsonify(new_fornecedor), HTTPStatus.CREATED


    @staticmethod
    def update(fornecedor_id) -> FornecedorModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if not fornecedor:
            raise DataNotFound('Fornecedor')

        parser = reqparse.RequestParser()

        parser.add_argument("razao_social", type=str, store_missing=False)
        parser.add_argument("nome_fantasia", type=str, store_missing=False)
        parser.add_argument("cnpj", type=str, store_missing=False)
        parser.add_argument("inscricao_estadual", type=str, store_missing=False)
        parser.add_argument("contato", type=str, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(fornecedor, key, value)
        
        fornecedor.save()
        return jsonify(fornecedor), HTTPStatus.OK

