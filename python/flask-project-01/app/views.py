from flask import render_template
from app import app
from forms import LoginForm
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ruslan'}    # user
    groups = ['Unix', 'Windows', 'QA']
    uri = request.uri
    return render_template("index.html", title = 'Home', user = user, groups = groups)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Sing In', form=form)




