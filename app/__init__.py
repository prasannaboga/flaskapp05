""" init file for app """

from flask import Flask
from app.api import API_BP
from app.models import db, ma
from app.pages.views import pages

import logging
import logging.handlers

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

    # init libraries
    db.init_app(app)
    ma.init_app(app)

    app.config['BUNDLE_ERRORS'] = True

    # logging
    handler = logging.handlers.RotatingFileHandler(
        'logs/{}.log'.format(app.config['ENV']),
        maxBytes=1024*1024,
        backupCount=20
    )
    handler.setLevel(app.config['LOGGER_LEVEL'])
    app.logger.addHandler(handler)

    # register blueprints
    app.register_blueprint(pages)
    app.register_blueprint(API_BP, url_prefix='/api')

    return app
