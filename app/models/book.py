from datetime import datetime
from app.models import db, ma


class Book(db.Document):
    meta = {'collection': 'books'}
    title = db.StringField(required=True, min_length=3, max_length=140, unique=True)
    description = db.StringField(required=True, max_length=200)
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<Book - {}>'.format(self.title)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)


class BookSchema(ma.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')


