from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from bson import ObjectId
from marshmallow import Schema, fields

db = MongoEngine()
ma = Marshmallow()

Schema.TYPE_MAPPING[ObjectId] = fields.String
