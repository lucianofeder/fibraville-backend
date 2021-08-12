from datetime import timedelta
from flask import Flask
from environs import Env
from app.configs import api, database, migration, jwt
from flask_cors import CORS


def create_app() -> Flask:
    env = Env()
    env.read_env

    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=4)
    

    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    return app
