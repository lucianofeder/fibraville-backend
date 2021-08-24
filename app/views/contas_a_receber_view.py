from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.contas_a_receber_service import ContasAReceberService


class ContasAReceberResource(Resource):

    # @jwt_required() => apenas admin
    def get(self):
        response, response.status_code = ContasAReceberService.get_all()
        return response


class ContasAReceberRetrieveResource(Resource):

    # @jwt_required() => apenas admin ou se a conta permanecer ao proprio usuario
    def get(self, conta_id):
        response, response.status_code = ContasAReceberService.get_by_id(conta_id)
        return response
    

    # @jwt_required() => apenas admin
    def patch(self, conta_id):
        response, response.status_code = ContasAReceberService.update(conta_id)
        return response

    
    # @jwt_required() => apenas admin
    def delete(self, conta_id):
        response, response.status_code = ContasAReceberService.delete(conta_id)
        return response


class ContasAReceberPayBillResource(Resource):

    # @jwt_required()
    def put(self, conta_id):
        response, response.status_code = ContasAReceberService.pay_bill(conta_id)
        return response


class ContasAReceberByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        response, response.status_code = ContasAReceberService.get_by_usuario_id(usuario_id)
        return response

    # @jwt_required()
    def post(self, usuario_id):
        try:
            response, response.status_code = ContasAReceberService.create(usuario_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

