from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.visita_tecnica_service import VisitaTecnicaService


class VisitaTecnicaResource(Resource):

    # @jwt_required()
    def get(self):
        return make_response(VisitaTecnicaService.get_all())

    def post(self):
        return make_response(VisitaTecnicaService.create())


class VisitaTecnicaRetrieveResource(Resource):

    # @jwt_required()
    def get(self, visita_tecnica_id):
        return make_response(VisitaTecnicaService.get_by_id(visita_tecnica_id))
    

    # @jwt_required()
    def patch(self, visita_tecnica_id):
        try:
            return make_response(VisitaTecnicaService.update(visita_tecnica_id))
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, visita_tecnica_id):
        return make_response(VisitaTecnicaService.delete(visita_tecnica_id))
