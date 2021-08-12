from flask import Flask
from flask_restful import Api


def init_app(app: Flask) -> None:
    api = Api(app)

    from app.models.usuario_model import UsuarioModel
    from app.models.usuario_nao_registrado_model import UsuarioNaoRegistradoModel