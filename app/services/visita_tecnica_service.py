from datetime import datetime
from app.models.visita_tecnica_model import VisitaTecnicaModel
from app.models.produto_model import ProdutoModel
from app.models.usuario_model import UsuarioModel

from app.services.visita_tecnica_produto_service import VisitaTecnicaProdutoService
from app.services.visita_tecnica_tecnico_service import VisitaTecnicaTecnicoService

from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus

import ipdb

class VisitaTecnicaService:

    @staticmethod
    def get_all():
        visitas_list = VisitaTecnicaModel.query.all()
        return jsonify([{
            "id": visita.id,
            "data_agendamento": visita.data_agendamento,
            "duracao_estimada": visita.duracao_estimada,
            "observacao": visita.observacao,
            "ordem_servico_id": visita.ordem_servico_id
        } for visita in visitas_list]), HTTPStatus.OK 


    @staticmethod
    def get_by_id(visita_id) -> VisitaTecnicaModel:
        visita = VisitaTecnicaModel.query.get(visita_id)
        if visita:
            return jsonify(visita.serializer()), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> VisitaTecnicaModel:
        parser = reqparse.RequestParser()

        parser.add_argument("data_agendamento", type=str, required=True)
        parser.add_argument("duracao_estimada", type=int)
        parser.add_argument("observacao", type=str)
        parser.add_argument("ordem_servico_id", type=int, required=True)
        parser.add_argument("produtos_list", required=True, type=list, location='json')
        parser.add_argument("tecnicos_list", required=True, type=list, location='json')


        data = parser.parse_args(strict=True)

        data['data_agendamento'] = datetime.fromisoformat(data['data_agendamento'])

        produtos_list = data.pop('produtos_list')
        tecnicos_list = data.pop('tecnicos_list')

        new_visita: VisitaTecnicaModel = VisitaTecnicaModel(**data)
        new_visita.save()

        VisitaTecnicaProdutoService.relate_visita_produtos_list(visita_id=new_visita.id, produtos_dict_list=produtos_list)
        visita = VisitaTecnicaTecnicoService.relate_visita_tecnico_list(visita_id=new_visita.id, tecnicos_id_list=tecnicos_list)
        visita.save()

        return jsonify(visita.serializer()), HTTPStatus.CREATED


    @staticmethod
    def update(visita_id) -> VisitaTecnicaModel:        
        parser = reqparse.RequestParser()

        parser.add_argument("data_agendamento", type=str, store_missing=False)
        parser.add_argument("duracao_estimada", type=int, store_missing=False)
        parser.add_argument("observacao", type=str, store_missing=False)
        parser.add_argument("ordem_servico_id", type=int, store_missing=False)
        parser.add_argument("produtos_list", type=list, location='json', store_missing=False)
        parser.add_argument("tecnicos_list", type=list, location='json', store_missing=False)

        data = parser.parse_args(strict=True)
        
        visita = VisitaTecnicaModel.query.get(visita_id)
        if not visita:
            raise DataNotFound('Visita tecnica')


        if 'produtos_list' in data:
            produtos_list = data.pop('produtos_list')

        if 'tecnicos_list' in data:
            tecnicos_list = data.pop('tecnicos_list')

        if 'produtos_list' in data:
            visita = VisitaTecnicaProdutoService.relate_visita_produtos_list(visita_id=visita_id, produtos_dict_list=produtos_list)
        
        if 'tecnicos_list' in data:
            visita = VisitaTecnicaTecnicoService.update_visita_tecnico_list(visita_id=visita_id, tecnicos_id_list=tecnicos_list)
        
        for key, value in data.items():
            setattr(visita, key, value)
        
        visita.save()
        return jsonify(visita.serializer()), HTTPStatus.OK

    
    @staticmethod
    def delete(visita_id) -> None:
        visita = VisitaTecnicaModel.query.get(visita_id)
        if visita:
            visita.delete()
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND
