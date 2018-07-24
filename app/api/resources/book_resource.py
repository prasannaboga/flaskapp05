""" Book Resource """
from flask import request
from flask_restful import Resource, reqparse
from mongoengine import ValidationError, NotUniqueError

from app.api.auth import auth
from app.models.book import Book, BookSchema


parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help='Cannot be blank')
parser.add_argument('description', type=str, help='Some description about book')


# class BookResource(Resource):
#     """ Book Resource Class """
#
#     def get(self, id):
#         book = Book.objects.get(id=id)
#         book_schema = BookSchema()
#         return {'status': 'success', 'data': book_schema.dump(book).data}, 200
#
#     def put(self, id):
#         pass
#
#     def delete(self, id):
#         pass


class BooksResource(Resource):
    decorators = [auth.login_required]
    def get(self):
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 3))
        paginate_books = Book.objects.paginate(page=page, per_page=per_page)
        books_schema = BookSchema(many=True)
        return {'status': 'success', 'data': books_schema.dump(paginate_books.items).data}, 200


    def post(self):
        errors = {}
        status_code = 201

        data = self.parser.parse_args()
        book = Book(
            title=data['title'],
            description=data['description']
        )

        try:
            book.save()
        except ValidationError as error:
            status_code = 400
            errors = error.to_dict()
        except NotUniqueError:
            status_code = 400
            errors = {'book': 'Unique validation error..!'}

        if book.id is None:
            return {'status': 'failed', 'errors': errors}, status_code
        else:
            book_schema = BookSchema()
            return {'status': 'success', 'data': book_schema.dump(book).data}, 201
