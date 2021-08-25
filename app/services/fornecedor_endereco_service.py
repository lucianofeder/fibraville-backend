from app.exc import DataNotFound
from app.models.fornecedor_endereco_model import FornecedorEnderecoModel
from app.models.fornecedor_model import FornecedorModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class FornecedorEnderecoService:

    @staticmethod
    def get_all():
        enderecos_list = FornecedorEnderecoModel.query.all()
        return jsonify(enderecos_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(endereco_id) -> FornecedorEnderecoModel:
        endereco = FornecedorEnderecoModel.query.get(endereco_id)
        if endereco:
            return jsonify(endereco), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> FornecedorEnderecoModel:
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

        return new_fornecedor


    @staticmethod
    def update(endereco_id) -> FornecedorEnderecoModel:
        endereco = FornecedorEnderecoModel.query.get(endereco_id)
        if not endereco:
            raise DataNotFound('Endereco fornecedor')

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

        for key, value in data.items():
            setattr(endereco, key, value)
        
        endereco.save()
        return endereco

    
    @staticmethod
    def delete(endereco_id) -> None:
        fornecedor = FornecedorEnderecoModel.query.get(endereco_id)
        if fornecedor:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_fornecedor_id(fornecedor_id) -> FornecedorEnderecoModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        if not fornecedor:
            raise DataNotFound('Fornecedor')
        return jsonify(fornecedor.endereco_fornecedor), HTTPStatus.OK