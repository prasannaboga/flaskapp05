from app import create_app

import json


def test_config():
    assert not create_app().testing
    assert create_app({
        'TESTING': True,
        'ENV': 'testing',
        'MONGODB_HOST_URI': 'mongodb://localhost:27017/flaskapp05_development',
        'LOGGER_LEVEL': 10
    }).testing


def test_pages(client):
    # TODO implement properly
    response = client.get('/')
    assert 200 == response.status_code


def test_api(client):
    response = client.get('/api')
    assert 200 == response.status_code

    json_data = json.loads(response.data)
    assert 'status' in json_data
    assert 'ok' == json_data['status']


def test_api_config(client):
    response = client.get('/api/config')
    assert 200 == response.status_code

    json_data = json.loads(response.data)
    assert 'ENV' in json_data
    assert 'testing' == json_data['ENV']
