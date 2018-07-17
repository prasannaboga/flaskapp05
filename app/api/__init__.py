from flask import Blueprint, jsonify
from flask_restful import Api
from app.api.resources.config_resource import ConfigResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(ConfigResource, '/config')


@api_bp.route('')
def index():
    return jsonify({'status': 'ok'})
