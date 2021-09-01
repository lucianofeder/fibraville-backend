from app.models.contrato_model import ContratoModel
from app.models.plano_model import PlanoModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class ContratoService:

    @staticmethod
    def get_all():
        contratos_list = ContratoModel.query.all()
        return jsonify(contratos_list), HTTPStatus.OK 

    @staticmethod
    def get_by_id(contrato_id) -> ContratoModel:
        conta = ContratoModel.query.get(contrato_id)
        if conta:
            return jsonify(conta), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND



    @staticmethod
    def create() -> ContratoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("duracao_meses", type=int, required=True)
        parser.add_argument("plano_id", type=int)

        data = parser.parse_args(strict=True)

        if data.plano_id:
            plano = PlanoModel.query.get(data.plano_id)
            if not plano:
                raise DataNotFound('Plano')

        new_contrato: ContratoModel = ContratoModel(**data)
        new_contrato.save()

        return jsonify(new_contrato), HTTPStatus.CREATED


    @staticmethod
    def update(contrato_id) -> ContratoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, store_missing=False)
        parser.add_argument("duracao_meses", type=int, store_missing=False)
        parser.add_argument("plano_id", type=int, store_missing=False)

        data = parser.parse_args(strict=True)

        contrato = ContratoModel.query.get(contrato_id)
        for key, value in data.items():
            setattr(contrato, key, value)
        
        contrato.save()
        return jsonify(contrato), HTTPStatus.OK

    
    @staticmethod
    def delete(contrato_id) -> None:
        endereco = ContratoModel.query.get(contrato_id)
        if endereco:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND
