from http import HTTPStatus
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from flask import make_response

from app.services.usuario_permissao_service import UsuarioPermissaoService
    

class UsuarioPermissaoRetrieveResource(Resource):
    # jwt_required()
    def get(self, usuario_id):
        return make_response(UsuarioPermissaoService.get_by_user_id(usuario_id))
    
    # jwt_required() => Apenas usuarios administradores
    def patch(self, usuario_id):
        return make_response(UsuarioPermissaoService.update(usuario_id))
