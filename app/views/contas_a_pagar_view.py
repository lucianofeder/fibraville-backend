from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.contas_a_pagar_service import ContasAPagarService


class ContasAPagarResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(ContasAPagarService.get_all())


class ContasAPagarRetrieveResource(Resource):

    # @jwt_required()
    def get(self, conta_id):
        return make_response(ContasAPagarService.get_by_id(conta_id))
    

    # @jwt_required()
    def patch(self, conta_id):
        try:
            return make_response(ContasAPagarService.update(conta_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, conta_id):
        return make_response(ContasAPagarService.delete(conta_id))


class ContasAPagarPayBillResource(Resource):

    # @jwt_required()
    def put(self, conta_id):
        try:
            return make_response(ContasAPagarService.pay_bill(conta_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class ContasAPagarByFornecedorResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        return make_response(ContasAPagarService.get_by_fornecedor_id(fornecedor_id))


    # @jwt_required()
    def post(self, fornecedor_id):
        try:
            return make_response(ContasAPagarService.create(fornecedor_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

