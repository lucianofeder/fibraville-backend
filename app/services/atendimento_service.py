from app.models.atendimento_model import AtendimentoModel
from app.models.usuario_model import UsuarioModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime
from app.services.helper import BaseServices


class AtendimentoService(BaseServices):
    model = AtendimentoModel


    @staticmethod
    def create() -> AtendimentoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("data", type=datetime)
        parser.add_argument("descricao", type=str, required=True)
        parser.add_argument("setor", type=str)
        parser.add_argument("usuario_cpf", type=str)
        parser.add_argument("usuario_telefone", type=str)
        parser.add_argument("usuario_id", type=int)
        parser.add_argument("ordem_servico_id", type=int)

        data = parser.parse_args(strict=True)

        if data.usuario_id:
            usuario = UsuarioModel.query.get(data.usuario_id)
            if not usuario:
                raise DataNotFound('Usuario')
            data.usuario_cpf = usuario.cpf


        if data.usuario_cpf and not data.usuario_id:
            usuario = UsuarioModel.query.filter(cpf=data.usuario_cpf).first()
            if usuario:
                data.usuario_cpf = usuario.cpf


        new_atendimento: AtendimentoModel = AtendimentoModel(**data)
        new_atendimento.save()

        return jsonify(new_atendimento), HTTPStatus.CREATED


    @staticmethod
    def update(atendimento_id) -> AtendimentoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("data", type=datetime, store_missing=False)
        parser.add_argument("descricao", type=str, store_missing=False)
        parser.add_argument("setor", type=str, store_missing=False)
        parser.add_argument("usuario_cpf", type=str, store_missing=False)
        parser.add_argument("usuario_telefone", type=str, store_missing=False)
        parser.add_argument("usuario_id", type=int, store_missing=False)
        parser.add_argument("ordem_servico_id", type=int, store_missing=False)

        data = parser.parse_args(strict=True)

        atendimento = AtendimentoModel.query.get(atendimento_id)

        if not atendimento:
            raise DataNotFound("Atendimento")

        for key, value in data.items():
            setattr(atendimento, key, value)
        
        atendimento.save()
        return jsonify(atendimento), HTTPStatus.OK

    
    @staticmethod
    def get_by_usuario(usuario_id) -> AtendimentoModel:

        usuario = UsuarioModel.query.get(usuario_id)
        if not usuario:
            raise DataNotFound('Usuario')

        atendimento = AtendimentoModel.query.filter_by(usuario_id=usuario_id).all()
        if atendimento:
            return jsonify(atendimento), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND
