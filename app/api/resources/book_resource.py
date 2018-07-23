""" Book Resource """
from flask import request
from flask_restful import Resource
from app.models.book import Book, BookSchema


class BookResource(Resource):
    """ Book Resource Class """
    def get(self, id=None):
        if id is None:
            page = int(request.args.get('page', 1))
            per_page = int(request.args.get('per_page', 3))
            paginate_books = Book.objects.paginate(page=page, per_page=per_page)
            books_schema = BookSchema(many=True)
            return {'status': 'success', 'data': books_schema.dump(paginate_books.items).data}, 200
        else:
            book = Book.objects.get(id=id)
            book_schema = BookSchema()
            return {'status': 'success', 'data': book_schema.dump(book).data}, 200
