from app.models.plano_model import PlanoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from app.services.helper import BaseServices

class PlanoService(BaseServices):
    model = PlanoModel


    @staticmethod
    def create_plano() -> PlanoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("velocidade", type=int, required=True)

        data = parser.parse_args(strict=True)

        new_plano: PlanoModel = PlanoModel(**data)
        new_plano.save()

        return jsonify(new_plano), HTTPStatus.CREATED

        