from flask_restful import Resource
from flask import current_app as app


class ConfigResource(Resource):
    def get(self):
        data = {}
        for key, value in sorted(app.config.items()):
            data[key] = str(value)

        return data
