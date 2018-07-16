from app import app
from flask import flash, redirect, render_template, request, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index', config=app.config)
