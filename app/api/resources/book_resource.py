""" Book Resource """
from flask import request, jsonify
from flask_restful import Resource
from app.models.book import Book, BookSchema

import json


class BookResource(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 3))
        paginated_books = Book.objects.paginate(page=page, per_page=per_page)
        books = []
        for _book in paginated_books.items:
            books.append(json.loads(_book.to_json()))
        return {'status': 'success', 'data': books}, 200


class BookAllResource(Resource):
    def get(self):
        books = Book.objects.all()
        books_schema = BookSchema(many=True)
        result = books_schema.dump(books)
        print('line 24')
        print(books_schema)
        print(jsonify(books))
        return {'status': 'success', 'data': jsonify(result.data)}, 200
