from app.exc import DataNotFound
from app.models.fornecedor_endereco_model import FornecedorEnderecoModel
from app.models.fornecedor_model import FornecedorModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices


class FornecedorEnderecoService(BaseServices):
    model =  FornecedorEnderecoModel


    @staticmethod
    def create(fornecedor_id) -> FornecedorEnderecoModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if not fornecedor:
            raise DataNotFound('Fornecedor')
        
        parser = reqparse.RequestParser()

        parser.add_argument("cep", type=str, required=True)
        parser.add_argument("rua", type=str, required=True)
        parser.add_argument("numero", type=str)
        parser.add_argument("bairro", type=str, required=True)
        parser.add_argument("cidade", type=str, required=True)
        parser.add_argument("estado", type=str, required=True)
        parser.add_argument("complemento", type=str)
        parser.add_argument("referencia", type=str)

        data = parser.parse_args(strict=True)

        new_fornecedor: FornecedorEnderecoModel = FornecedorEnderecoModel(**data)
        new_fornecedor.save()

        fornecedor.endereco_fornecedor_id = new_fornecedor.id
        fornecedor.save()

        return jsonify(new_fornecedor), HTTPStatus.CREATED


    @staticmethod
    def update(endereco_id) -> FornecedorEnderecoModel:
        endereco = FornecedorEnderecoModel.query.get(endereco_id)
        if not endereco:
            raise DataNotFound('Endereco fornecedor')

        parser = reqparse.RequestParser()

        parser.add_argument("cep", type=str, store_missing=False)
        parser.add_argument("rua", type=str, store_missing=False)
        parser.add_argument("numero", type=str, store_missing=False)
        parser.add_argument("bairro", type=str, store_missing=False)
        parser.add_argument("cidade", type=str, store_missing=False)
        parser.add_argument("estado", type=str, store_missing=False)
        parser.add_argument("complemento", type=str, store_missing=False)
        parser.add_argument("referencia", type=str, store_missing=False)

        data = parser.parse_args(strict=True)

        for key, value in data.items():
            setattr(endereco, key, value)
        
        endereco.save()
        return jsonify(endereco), HTTPStatus.OK


    @staticmethod
    def get_by_fornecedor_id(fornecedor_id) -> FornecedorEnderecoModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if not fornecedor:
            raise DataNotFound('Fornecedor')
        return jsonify(fornecedor.endereco_fornecedor), HTTPStatus.OK