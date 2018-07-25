from flask import current_app as app
from flask import Blueprint, render_template

pages = Blueprint('pages', __name__, url_prefix='', template_folder='templates')


@pages.route('/')
@pages.route('/index')
def index():
    # Testing logging levels
    app.logger.warning('I AM WARNING***')
    app.logger.debug('I AM DEBUG***')
    app.logger.error('I AM ERROR***')
    app.logger.info('I AM INFO***')
    return render_template('index.html', config=app.config)
