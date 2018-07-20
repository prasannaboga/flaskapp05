import datetime

from faker import Faker

from app import create_app, db
from app.models.book import Book

app = create_app(None)
faker = Faker()


def seed_books_data(db):
    try:
        for i in range(5):
            book = Book(title=faker.company(), description=faker.sentence(nb_words=18))
            book.save()
    except Exception as e:
        print('Error while seed books data - {0}'.format(e))


def seed_db(app):
    with app.app_context():
        seed_books_data(db)


if __name__ == '__main__':
    seed_db(app)
