from flask import Blueprint, g, jsonify, make_response
from flask_restful import Api

from app.api.resources.config_resource import ConfigResource
from app.api.resources.book_resource import BooksResource
from app.api.auth import auth


API_BP = Blueprint('api', __name__)
API = Api(API_BP)

API.add_resource(ConfigResource, '/config')
API.add_resource(BooksResource, '/books')


@API_BP.route('')
def index():
    return jsonify({'status': 'ok'})


@API_BP.route('/auth/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii')})
