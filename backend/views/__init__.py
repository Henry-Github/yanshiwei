import os
from flask_restful import Api
from flask import send_from_directory
from .checks import Checks
from flask import Flask
from flask_cors import CORS
import flask_restful

FILE_ROOT = os.getcwd()
static_path = os.path.abspath(os.path.join(FILE_ROOT, '../frontend/dist'))

print(static_path)

__all__ = [
    'build_app'
]


def __gen_path(cls):
    return f'/api/{cls.__name__.lower()}'


def add_api(api: Api):
    api.add_resource(Checks, __gen_path(Checks))


def route_web(route_path: str):
    if len(route_path) == 0:
        return send_from_directory(static_path, 'index.html')
    else:
        return send_from_directory(static_path, route_path)


def build_app():
    app = Flask(__name__, static_folder=os.path.join(FILE_ROOT, '../frontend/dist/static'))
    CORS(app)
    api = flask_restful.Api(app)
    add_api(api)

    @app.route('/')
    def route_index():
        return route_web('')

    @app.route('/<path:path>', methods=['GET'])
    def all_route(path):
        return route_web(path)

    return app
