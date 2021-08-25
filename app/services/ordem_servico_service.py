from app.models.ordem_servico_model import OrdemServicoModel
from app.models.usuario_model import UsuarioModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime

class OrdemServicoService:

    @staticmethod
    def get_all():
        ordens_servico_list = OrdemServicoModel.query.all()
        return jsonify(ordens_servico_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(os_id) -> OrdemServicoModel:
        os = OrdemServicoModel.query.get(os_id)
        if os:
            return jsonify(os), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> OrdemServicoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float)
        parser.add_argument("proposito", type=str, required=True)
        parser.add_argument("descricao", type=str)
        parser.add_argument("finalizado", type=bool, default=False)
        parser.add_argument("usuario_id", type=int, required=True)

        data = parser.parse_args(strict=True)
        data.data_abertura = datetime.utcnow()

        usuario = UsuarioModel.query.get(data.usuario_id)
        if not usuario:
            raise DataNotFound('Usuario')

        new_os: OrdemServicoModel = OrdemServicoModel(**data)
        new_os.save()

        return new_os


    @staticmethod
    def update(os_id) -> OrdemServicoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float)
        parser.add_argument("proposito", type=str)
        parser.add_argument("descricao", type=str)

        data = parser.parse_args(strict=True)

        atendimento = OrdemServicoModel.query.get(os_id)
        for key, value in data.items():
            setattr(atendimento, key, value)
        
        atendimento.save()
        return atendimento

    
    @staticmethod
    def delete(os_id) -> None:
        os = OrdemServicoModel.query.get(os_id)
        if os:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def get_by_usuario(usuario_id) -> OrdemServicoModel:

        usuario = UsuarioModel.query.get(usuario_id)
        if not usuario:
            raise DataNotFound('Usuario')

        atendimento = OrdemServicoModel.query.filter(usuario_id=usuario_id)
        if atendimento:
            return jsonify(atendimento), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND