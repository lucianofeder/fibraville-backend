from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.contas_a_receber_service import ContasAReceberService


class ContasAReceberResource(Resource):

    # @jwt_required() => apenas admin
    def get(self):
        return make_response(ContasAReceberService.get_all())


class ContasAReceberRetrieveResource(Resource):

    # @jwt_required() => apenas admin ou se a conta permanecer ao proprio usuario
    def get(self, conta_id):
        return make_response(ContasAReceberService.get_by_id(conta_id))
    

    # @jwt_required() => apenas admin
    def patch(self, conta_id):
        try:
            return make_response(ContasAReceberService.update(conta_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND
    
    # @jwt_required() => apenas admin
    def delete(self, conta_id):
        return make_response(ContasAReceberService.delete(conta_id))


class ContasAReceberPayBillResource(Resource):

    # @jwt_required()
    def put(self, conta_id):
        return make_response(ContasAReceberService.pay_bill(conta_id))


class ContasAReceberByUsuarioResource(Resource):

    # @jwt_required()
    def get(self, usuario_id):
        return make_response(ContasAReceberService.get_by_usuario_id(usuario_id))

    # @jwt_required()
    def post(self, usuario_id):
        try:
            return make_response(ContasAReceberService.create(usuario_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

