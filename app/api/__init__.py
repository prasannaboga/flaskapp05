from flask import Blueprint, g, jsonify, make_response
from flask import current_app as app
from flask_restful import Api

from app.api.resources.config_resource import ConfigResource
from app.api.resources.book_resource import BooksResource, BookResource
from app.api.auth import auth


API_BP = Blueprint('api', __name__)
API = Api(API_BP)

API.add_resource(ConfigResource, '/config')
API.add_resource(BooksResource, '/books')
API.add_resource(BookResource, '/books/<id>')


@API_BP.route('')
def index():
    # Testing logging levels
    app.logger.warning('I AM WARNING***')
    app.logger.debug('I AM DEBUG***')
    app.logger.error('I AM ERROR***')
    app.logger.info('I AM INFO***')
    return jsonify({'status': 'ok'})


@API_BP.route('/auth/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii')})
