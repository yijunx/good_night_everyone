from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'tom'}
    posts = [{
        'author': {'username': 'willow'},
        'body': 'beatiful day!'
    }, {
        'author': {'username': 'emily'},
        'body': 'not beatiful day!'
    }]
    return render_template('index.html', title='home', user=user, posts=posts)