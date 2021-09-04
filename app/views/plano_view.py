from http import HTTPStatus
from flask.helpers import make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import jsonify

from app.services.plano_service import PlanoService
from app.models.plano_model import PlanoModel


class PlanoResource(Resource):
    def get(self):
        return make_response(PlanoService.get_all())
    

    # @jwt_required() # apenas usuario admin
    def post(self):
        return make_response(PlanoService.create_plano())


class PlanoRetrieveResource(Resource):
    def get(self, plano_id: int):
        return make_response(PlanoService.get_by_id(plano_id))
    
    # jwt_required() # apenas usuario admin
    def delete(self, plano_id: int):
        return make_response(PlanoService.delete(plano_id))
