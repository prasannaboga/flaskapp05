from flask import Blueprint, jsonify
from flask_restful import Api
from app.api.resources.config_resource import ConfigResource
from app.api.resources.book_resource import BookResource, BookAllResource


API_BP = Blueprint('api', __name__)
API = Api(API_BP)

API.add_resource(ConfigResource, '/config')
API.add_resource(BookResource, '/books')
API.add_resource(BookAllResource, '/books/all')


@API_BP.route('')
def index():
    return jsonify({'status': 'ok'})
