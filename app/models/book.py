from datetime import datetime
from app.models import db, ma


class Book(db.Document):
    meta = {'collection': 'books'}
    title = db.StringField(required=True, max_length=140)
    description = db.StringField(max_length=200, default='')
    created_at = db.DateTimeField(default=datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return '<Book - {}>'.format(self.title)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)


class BookSchema(ma.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')


