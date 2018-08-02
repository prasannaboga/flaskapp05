import os
import tempfile

import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'ENV': 'testing',
        'MONGODB_HOST_URI': 'mongodb://localhost:27017/flaskapp05_development',
        'LOGGER_LEVEL': 10
    })

    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
