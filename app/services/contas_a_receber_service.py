from app.models.contas_a_receber_model import ContasAReceberModel
from app.models.usuario_model import UsuarioModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime, date

class ContasAReceberService:

    @staticmethod
    def get_all():
        contas_list = ContasAReceberModel.query.all()
        return jsonify(contas_list), HTTPStatus.OK 

    @staticmethod
    def get_by_id(conta_id) -> ContasAReceberModel:
        conta = ContasAReceberModel.query.get(conta_id)
        if conta:
            return jsonify(conta), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND

    @staticmethod
    def update(conta_id) -> ContasAReceberModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float)
        parser.add_argument("data_a_pagar", type=datetime)
        parser.add_argument("data_pago", type=datetime)
        parser.add_argument("nfe", type=str)
        parser.add_argument("usuario_id", type=int)
        parser.add_argument("pago", type=bool)

        data = parser.parse_args(strict=True)

        conta = ContasAReceberModel.query.get(conta_id)
        if not conta:
            raise DataNotFound('Conta')

        for key, value in data.items():
            setattr(conta, key, value)
        
        conta.save()
        return conta


    @staticmethod
    def pay_bill(conta_id):
        conta = ContasAReceberModel.query.get(conta_id)
        if conta:
            conta.pago = True
            conta.data_pago = datetime.utcnow()
            conta.save()
            return {}, HTTPStatus.ACCEPTED
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def delete(conta_id) -> None:
        endereco = ContasAReceberModel.query.get(conta_id)
        if endereco:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_usuario_id(usuario_id):
        contas_list = ContasAReceberModel.query.filter(usuario_id=usuario_id)
        if contas_list:
            return jsonify({"usuario_id": usuario_id, "contas_list": contas_list}), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(usuario_id) -> ContasAReceberModel:
        usuario = UsuarioModel.query.get(usuario_id)
        
        if not usuario:
            raise DataNotFound('Usuario')
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("data_a_pagar", type=date, required=True)
        parser.add_argument("data_pago", type=datetime)
        parser.add_argument("pago", type=bool, default=False)

        data = parser.parse_args(strict=True)

        new_conta_a_receber: ContasAReceberModel = ContasAReceberModel(**data, usuario_id=usuario_id)
        new_conta_a_receber.save()

        return new_conta_a_receber

