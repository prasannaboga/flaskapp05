""" init file for app """

from flask import Flask
from app.api import API_BP
from app.models import db
from app.pages.views import pages


def create_app(test_config=None):
    """ init app """
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config['MONGODB_SETTINGS'] = {
        'host': app.config['MONGODB_HOST_URI']
    }

    db.init_app(app)
    app.register_blueprint(pages)
    app.register_blueprint(API_BP, url_prefix='/api')

    return app
