from app.models.contas_a_receber_model import ContasAReceberModel
from app.models.usuario_model import UsuarioModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime
from app.services.helper import BaseServices


class ContasAReceberService(BaseServices):
    model = ContasAReceberModel


    @staticmethod
    def update(conta_id) -> ContasAReceberModel:
        conta = ContasAReceberModel.query.get(conta_id)
        if not conta:
            raise DataNotFound('Conta')

        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, store_missing=False)
        parser.add_argument("data_a_pagar", type=datetime, store_missing=False)
        parser.add_argument("data_pago", type=datetime, store_missing=False)
        parser.add_argument("usuario_id", type=int, store_missing=False)

        data = parser.parse_args(strict=True)

        if 'usuario_id' in data:
            usuario = UsuarioModel.query.get(data.usuario_id)
            if not usuario:
                raise DataNotFound('Usuario')

        if 'data_a_pagar' in data:
            data['data_a_pagar'] = datetime.fromisoformat(data['data_a_pagar'])

        if 'data_pago' in data:
            data['data_pago'] = datetime.fromisoformat(data['data_pago'])

        for key, value in data.items():
            setattr(conta, key, value)
        
        conta.save()
        return jsonify(conta)


    @staticmethod
    def pay_bill(conta_id):
        conta = ContasAReceberModel.query.get(conta_id)
        if conta:
            conta.data_pago = datetime.utcnow()
            conta.save()
            return {}, HTTPStatus.ACCEPTED
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def get_by_usuario_id(usuario_id):
        contas_list = ContasAReceberModel.query.filter_by(usuario_id=usuario_id).all()
        if contas_list:
            return jsonify(BaseServices.paginate(contas_list)), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create(usuario_id) -> ContasAReceberModel:
        usuario = UsuarioModel.query.get(usuario_id)
        
        if not usuario:
            raise DataNotFound('Usuario')
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("data_a_pagar", type=str, required=True)
        parser.add_argument("data_pago", type=datetime, store_missing=False)

        data = parser.parse_args(strict=True)

        data['data_a_pagar'] = datetime.fromisoformat(data['data_a_pagar'])

        if 'data_pago' in data:
            data['data_pago'] = datetime.fromisoformat(data['data_pago'])

        new_conta_a_receber: ContasAReceberModel = ContasAReceberModel(**data, usuario_id=usuario_id)
        new_conta_a_receber.save()

        return jsonify(new_conta_a_receber), HTTPStatus.CREATED

