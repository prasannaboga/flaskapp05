""" Book Resource """
from flask import request
from flask_restful import Resource
from app.models.book import Book

import json


class BookResource(Resource):
    def get(self):
        page = int(request.args.get('page'))
        per_page = int(request.args.get('per_page'))
        paginated_books = Book.objects.paginate(page=page, per_page=per_page)
        books = []
        for _book in paginated_books.items:
            books.append(json.loads(_book.to_json()))
        return {'status': 'success', 'data': books}, 200
