from flask import Flask
from app.pages.views import pages


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.register_blueprint(pages)

    return app
