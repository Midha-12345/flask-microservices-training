from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import load_configuration

app = Flask(__name__)
load_configuration(app)

class CustomApi(Api):
    def handle_error(self, e):
        return {'code': e.code, 'message': 'error', 'errors': e.message}, e.code
restful_api = CustomApi(app)

db = SQLAlchemy(app)