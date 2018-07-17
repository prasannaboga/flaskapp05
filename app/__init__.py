from flask import Flask
from app.pages.views import pages
from app.api import api_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(pages)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
