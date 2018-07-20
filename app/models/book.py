from datetime import datetime
from mongoengine import StringField, BooleanField
from app import db


class Book(db.Document):
    meta = {'collection': 'books'}
    title = StringField(required=True, max_length=140)
    description = StringField(max_length=200, default='')
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<Book - {}>'.format(self.title)

    def __str__(self):
        return self.title

    @property
    def _id(self):
        return str(self.id)

