from flask import Blueprint, jsonify
from flask_restful import Api
from app.api.resources.config_resource import ConfigResource
from app.api.resources.book_resource import BookResource


API_BP = Blueprint('api', __name__)
API = Api(API_BP)

API.add_resource(ConfigResource, '/config')
API.add_resource(BookResource, '/books')


@API_BP.route('')
def index():
    return jsonify({'status': 'ok'})
