from app.models.contas_a_pagar_model import ContasAPagarModel
from app.models.contas_a_pagar_model import ContasAPagarModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime, date

class ContasAPagarService:

    @staticmethod
    def get_all():
        enderecos = ContasAPagarModel.query.all()
        return jsonify(enderecos), HTTPStatus.OK 

    @staticmethod
    def get_by_id(conta_id) -> ContasAPagarModel:
        conta = ContasAPagarModel.query.get(conta_id)
        if conta:
            return jsonify(conta), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND

    @staticmethod
    def update(conta_id) -> ContasAPagarModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=str, required=True)
        parser.add_argument("data_emissao", type=datetime, required=True)
        parser.add_argument("data_a_pagar", type=date, required=True)
        parser.add_argument("nfe", type=str)
        parser.add_argument("n_documento", type=str)
        parser.add_argument("pago", type=bool, default=False)

        data = parser.parse_args(strict=True)

        conta = ContasAPagarModel.query.get(conta_id)
        for key, value in data.items():
            setattr(conta, key, value)
        
        conta.save()
        return conta


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
        endereco = ContasAPagarModel.query.get(conta_id)
        if endereco:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_fornecedor_id(fornecedor_id):
        contas_list = ContasAPagarModel.query.filter(fornecedor_id=fornecedor_id)
        if contas_list:
            return jsonify({"fornecedor_id": fornecedor_id, "contas_list": contas_list}), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(fornecedor_id) -> ContasAPagarModel:
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=str, required=True)
        parser.add_argument("data_digitado", type=datetime, default=datetime.utcnow())
        parser.add_argument("data_emissao", type=datetime, required=True)
        parser.add_argument("data_a_pagar", type=date, required=True)
        parser.add_argument("nfe", type=str)
        parser.add_argument("n_documento", type=str)
        parser.add_argument("pago", type=bool, default=False)

        data = parser.parse_args(strict=True)

        new_conta_a_pagar: ContasAPagarModel = ContasAPagarModel(**data, fornecedor_id=fornecedor_id)
        new_conta_a_pagar.save()

        return new_conta_a_pagar

