""" init file for app """

from flask import Flask
from app.api import API_BP
from app.models import db, ma
from app.pages.views import pages

import logging
import logging.handlers
import time

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
    handler = logging.handlers.TimedRotatingFileHandler(
        'logs/{}.log'.format(app.config['ENV']),
        backupCount=10,
        when='midnight',
        interval=1
    )
    log_message_formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s {%(filename)s:%(lineno)d} - %(message)s'
    )
    handler.setLevel(app.config['LOGGER_LEVEL'])
    handler.setFormatter(log_message_formatter)
    app.logger.addHandler(handler)

    # register blueprints
    app.register_blueprint(pages)
    app.register_blueprint(API_BP, url_prefix='/api')

    return app
