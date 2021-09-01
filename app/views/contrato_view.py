from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.contrato_service import ContratoService


class ContratoResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(ContratoService.get_all())

    def post(self):
        try:
            return make_response(ContratoService.create())
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND


class ContratoRetrieveResource(Resource):

    # @jwt_required()
    def get(self, contrato_id):
        return make_response(ContratoService.get_by_id(contrato_id))
    

    # @jwt_required()
    def patch(self, contrato_id):
        return make_response(ContratoService.update(contrato_id))

    
    # @jwt_required()
    def delete(self, contrato_id):
        return make_response(ContratoService.delete(contrato_id))

