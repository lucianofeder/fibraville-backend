from flask import Flask
from flask_caching import Cache


cache = Cache()

def init_app(app: Flask) -> None:
    cache.init_app(app)
    app.cache = cache