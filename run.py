from app import create_app, db
from app.models.book import Book

app = create_app(None)


if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {'app': app,
            'db': db,
            'Book': Book,
            'name': 'Prasanna'}
