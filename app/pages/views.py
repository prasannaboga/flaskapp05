from flask import current_app as app
from flask import Blueprint, render_template

pages = Blueprint('pages', __name__, url_prefix='', template_folder='templates')


@pages.route('/')
@pages.route('/index')
def index():
    return render_template('index.html', config=app.config)
