from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.contas_a_pagar_service import ContasAPagarService


class ContasAPagarResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = ContasAPagarService.get_all()
        return response


class ContasAPagarRetrieveResource(Resource):

    # @jwt_required()
    def get(self, conta_id):
        response, response.status_code = ContasAPagarService.get_by_id(conta_id)
        return response
    

    # @jwt_required()
    def patch(self, conta_id):
        response, response.status_code = ContasAPagarService.update(conta_id)
        return response

    
    # @jwt_required()
    def delete(self, conta_id):
        response, response.status_code = ContasAPagarService.delete(conta_id)
        return response


class ContasAPagarPayBillResource(Resource):

    # @jwt_required()
    def put(self, conta_id):
        response, response.status_code = ContasAPagarService.pay_bill(conta_id)


class ContasAPagarByFornecedorResource(Resource):

    # @jwt_required()
    def get(self, fornecedor_id):
        response, response.status_code = ContasAPagarService.get_by_fornecedor_id(fornecedor_id)
        return response

    # @jwt_required()
    def post(self, fornecedor_id):
        response, response.status_code = ContasAPagarService.create(fornecedor_id)
        return response


