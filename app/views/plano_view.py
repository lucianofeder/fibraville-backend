from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import jsonify

from app.services.plano_service import PlanoService


class PlanoResource(Resource):
    def get(self):
        response = jsonify(PlanoService.get_all())
        response.status_code = HTTPStatus.OK
        return response
    

    # @jwt_required() # apenas usuario admin
    def post(self):
        data, status = PlanoService.create_plano()
        response = data
        response.status_code = status
        return response


class PlanoRetrieveResource(Resource):
    def get(self, plano_id: int):
        return PlanoService.get_by_id(plano_id)
    
    # jwt_required() # apenas usuario admin
    def delete(self, plano_id: int):
        return PlanoService.delete(plano_id)
