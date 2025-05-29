from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Kevin"}
    posts = [
        {
            'author': {'username': 'Patrick'},
            'body': 'Great day to be alive!'
        },
        {
            'author': {'username': 'Le'},
            'body': 'I like to play Overwatch!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)