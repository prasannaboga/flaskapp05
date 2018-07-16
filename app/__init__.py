from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    return app


app = create_app()

from app import views