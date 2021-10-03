from datetime import timedelta
from flask import Flask
from environs import Env
from app.configs import api, database, migration, jwt, commands, mail, cache
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
    
    app.config["MAIL_SERVER"] = env("MAIL_SERVER")
    app.config["MAIL_PORT"] = env("MAIL_PORT")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = env("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = env("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = env("MAIL_USERNAME")
    app.config["MAIL_MAX_EMAILS"] = None
    app.config["MAIL_ASCII_ATTACHMENTS"] = False

    app.config["CACHE_TYPE"] = "SimpleCache"
    app.config["CACHE_DEFAULT_TIMEOUT"] = 300    

    database.init_app(app)
    migration.init_app(app)
    commands.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    api.init_app(app)

    return app
