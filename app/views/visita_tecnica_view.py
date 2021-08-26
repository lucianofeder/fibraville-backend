from http import HTTPStatus
from app.exc import DataNotFound
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.services.visita_tecnica_service import VisitaTecnicaService


class VisitaTecnicaResource(Resource):

    # @jwt_required()
    def get(self):
        response, response.status_code = VisitaTecnicaService.get_all()
        return response

    def post(self):
        response, response.status_code = VisitaTecnicaService.create()
        return response


class VisitaTecnicaRetrieveResource(Resource):

    # @jwt_required()
    def get(self, visita_id):
        response, response.status_code = VisitaTecnicaService.get_by_id(visita_id)
        return response
    

    # @jwt_required()
    def patch(self, visita_id):
        try:
            response, response.status_code = VisitaTecnicaService.update(visita_id)
            return response
        except DataNotFound as e:
            return e.message, HTTPStatus.NOT_FOUND

    
    # @jwt_required()
    def delete(self, visita_id):
        response, response.status_code = VisitaTecnicaService.delete(visita_id)
        return response
