from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask) -> None:
    Migrate(app, app.db)