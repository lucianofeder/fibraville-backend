from datetime import datetime
from app.models.visita_tecnica_model import VisitaTecnicaModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

class VisitaTecnicaService:

    @staticmethod
    def get_all():
        visitas_list = VisitaTecnicaModel.query.all()
        return jsonify(visitas_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(visita_id) -> VisitaTecnicaModel:
        visita = VisitaTecnicaModel.query.get(visita_id)
        if visita:
            return jsonify(visita), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> VisitaTecnicaModel:
        parser = reqparse.RequestParser()

        parser.add_argument("data_agendamento", type=str, required=True)
        parser.add_argument("duracao_estimada", type=int)
        parser.add_argument("observacao", type=str)
        parser.add_argument("ordem_servico_id", type=int, required=True)
        parser.add_argument("produtos_list", type=str, required=True)
        parser.add_argument("tecnicos_list", type=str, required=True)

        data = parser.parse_args(strict=True)

        new_visita: VisitaTecnicaModel = VisitaTecnicaModel(**data)
        new_visita.save()

        return new_visita


    @staticmethod
    def update(visita_id) -> VisitaTecnicaModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("nome", type=str)
        parser.add_argument("sobrenome", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("data_nascimento", type=datetime)
        parser.add_argument("e_pessoa_fisica", type=bool)
        parser.add_argument("cpf", type=str)
        parser.add_argument("cnpj", type=str)
        parser.add_argument("mae_nome", type=str)
        parser.add_argument("pai_nome", type=str)
        parser.add_argument("observacao", type=str)

        data = parser.parse_args(strict=True)
        
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita tecnica')
        
        for key, value in data.items():
            setattr(visita, key, value)
        
        visita.save()
        return visita

    
    @staticmethod
    def delete(visita_id) -> None:
        visita = VisitaTecnicaModel.query.get(visita_id)
        if visita:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND
