from app import create_app, db
from app.models.book import Book
from pymongo import MongoClient

app = create_app(None)
mongo_client = MongoClient()
pymongo_db = mongo_client[app.config['MONGODB_DATABASE']]


if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {'app': app,
            'db': db,
            'pymongo_db': pymongo_db,
            'Book': Book,
            'name': 'Prasanna'}
