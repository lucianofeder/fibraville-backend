from app.models.contas_a_pagar_model import ContasAPagarModel
from app.models.fornecedor_model import FornecedorModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime, date

class ContasAPagarService:

    @staticmethod
    def get_all():
        contas = ContasAPagarModel.query.all()
        return jsonify(contas), HTTPStatus.OK 

    @staticmethod
    def get_by_id(conta_id) -> ContasAPagarModel:
        conta = ContasAPagarModel.query.get(conta_id)
        if conta:
            return jsonify(conta), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND

    @staticmethod
    def update(conta_id) -> ContasAPagarModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, store_missing=False)
        parser.add_argument("data_emissao", type=datetime, store_missing=False)
        parser.add_argument("data_a_pagar", type=date, store_missing=False)
        parser.add_argument("nfe", type=str, store_missing=False)
        parser.add_argument("n_documento", type=str, store_missing=False)
        parser.add_argument("pago", type=bool, store_missing=False)

        data = parser.parse_args(strict=True)

        conta = ContasAPagarModel.query.get(conta_id)
        
        if not conta:
            raise DataNotFound('Conta')

        for key, value in data.items():
            setattr(conta, key, value)
        
        conta.save()
        return jsonify(conta), HTTPStatus.CREATED


    @staticmethod
    def pay_bill(conta_id):
        conta = ContasAPagarModel.query.get(conta_id)
        if conta:
            conta.pago = True
            conta.save()
            return {}, HTTPStatus.ACCEPTED
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def delete(conta_id) -> None:
        conta = ContasAPagarModel.query.get(conta_id)
        if conta:
            conta.delete()
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_fornecedor_id(fornecedor_id):
        contas_list = ContasAPagarModel.query.filter_by(fornecedor_id=fornecedor_id).all()
        if contas_list:
            return {"fornecedor_id": fornecedor_id, "contas_list": contas_list}, HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(fornecedor_id) -> ContasAPagarModel:
        fornecedor = FornecedorModel.query.get(fornecedor_id)
        
        if not fornecedor:
            raise DataNotFound('Fornecedor')

        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("data_digitado", type=datetime, default=datetime.utcnow())
        parser.add_argument("data_emissao", type=datetime, required=True)
        parser.add_argument("data_a_pagar", type=date, required=True)
        parser.add_argument("nfe", type=str)
        parser.add_argument("n_documento", type=str)
        parser.add_argument("pago", type=bool, default=False)

        data = parser.parse_args(strict=True)

        new_conta_a_pagar: ContasAPagarModel = ContasAPagarModel(**data, fornecedor_id=fornecedor_id)
        new_conta_a_pagar.save()

        return jsonify(new_conta_a_pagar), HTTPStatus.CREATED

