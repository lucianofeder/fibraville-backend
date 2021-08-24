from app.models.atendimento_model import AtendimentoModel
from app.models.usuario_model import UsuarioModel
from app.exc import DataNotFound
from flask_restful import reqparse
from flask import jsonify
from http import HTTPStatus
from datetime import datetime

class AtendimentoService:

    @staticmethod
    def get_all():
        atendimentos_list = AtendimentoModel.query.all()
        return jsonify(atendimentos_list), HTTPStatus.OK 


    @staticmethod
    def get_by_id(atendimento_id) -> AtendimentoModel:
        atendimento = AtendimentoModel.query.get(atendimento_id)
        if atendimento:
            return jsonify(atendimento), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND


    @staticmethod
    def create() -> AtendimentoModel:
        parser = reqparse.RequestParser()

        parser.add_argument("data", type=datetime, required=True)
        parser.add_argument("descricao", type=str, required=True)
        parser.add_argument("setor", type=str)
        parser.add_argument("usuario_cpf", type=str)
        parser.add_argument("usuario_telefone", type=str)
        parser.add_argument("usuario_id", type=int)
        parser.add_argument("ordem_servico_id", type=int, required=True)

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

        return new_atendimento


    @staticmethod
    def update(atendimento_id) -> AtendimentoModel:
        
        parser = reqparse.RequestParser()

        parser.add_argument("valor", type=float, required=True)
        parser.add_argument("duracao_meses", type=int, required=True)
        parser.add_argument("plano_id", type=int)

        data = parser.parse_args(strict=True)

        atendimento = AtendimentoModel.query.get(atendimento_id)
        for key, value in data.items():
            setattr(atendimento, key, value)
        
        atendimento.save()
        return atendimento

    
    @staticmethod
    def delete(atendimento_id) -> None:
        endereco = AtendimentoModel.query.get(atendimento_id)
        if endereco:
            return {}, HTTPStatus.NO_CONTENT
        return {}, HTTPStatus.NOT_FOUND

    
    @staticmethod
    def get_by_usuario(usuario_id) -> AtendimentoModel:

        usuario = UsuarioModel.query.get(usuario_id)
        if not usuario:
            raise DataNotFound('Usuario')

        atendimento = AtendimentoModel.query.filter(usuario_id=usuario_id)
        if atendimento:
            return jsonify(atendimento), HTTPStatus.OK
        return {}, HTTPStatus.NOT_FOUND
