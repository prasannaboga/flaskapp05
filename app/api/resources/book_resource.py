""" Book Resource """
from flask import jsonify
from flask_restful import Resource
from app.models.book import Book

import json


class BookResource(Resource):
    def get(self):
        # books = Book.objects.paginate(page=1, per_page=2)
        books = Book.objects.all()
        return {'status': 'success', 'data': json.loads(books.to_json())}, 200
