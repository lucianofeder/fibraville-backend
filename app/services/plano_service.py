from app.models.plano_model import PlanoModel
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class PlanoService:

    @staticmethod
    def get_all() -> list[PlanoModel]:
        data_list: list[PlanoModel] = PlanoModel.query.all()
        return [plano for plano in data_list]


    @staticmethod
    def get_by_id(id) -> PlanoModel:
        plano = PlanoModel.query.get(id)
        if plano:
            return jsonify(plano), HTTPStatus.CREATED
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create_plano() -> PlanoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("velocidade", type=int, required=True)

        data = parser.parse_args(strict=True)

        new_plano: PlanoModel = PlanoModel(**data)
        new_plano.save()

        return jsonify(new_plano), HTTPStatus.CREATED


    @staticmethod
    def delete(id) -> PlanoModel:
        plano = PlanoModel.query.get(id)
        if plano:
            plano.delete()
            return {"mensagem": "Plano deletado com sucesso"}, HTTPStatus.ACCEPTED
        return {"error": f"Plano com id:{id} nao encontrado"}, HTTPStatus.NOT_FOUND
        