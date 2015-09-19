#!/usr/bin/env python

from functools import wraps
from flask import Flask, request, Response
from flask.ext.pymongo import PyMongo
from wtforms import Form, BooleanField, TextField, PasswordField, validators

import logging


class RegistrationForm(Form):
    username = TextField('Username')
    email = TextField('Email Address')
    password = PasswordField('Password')
    #confirm = PasswordField('Repeat Password')


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 404 response that enables basic auth"""
    return Response(
        'Login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth \
            or not check_auth(auth.username, auth.password):
                return authenticate()
        return f(*args, **kwargs)
    return decorated


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
mongo = PyMongo(app)




@app.route("/")
#@require_auth
def hello_world():
    users = ""
    for user in mongo.db.users.find():
        users += "<li>%s</li>\n"% user
    #logging.warning(app.config["ADMIN_PASS"])
    return "Hello world<br>" \
        + " <a href='insert'>insert</a> " \
        + " <a href='register'>register?a=1&b=2&c=3</a> " \
        + " <ul> " + users + "</ul>" \
        + " <a href='http://flask.pocoo.org/snippets/8/'>doc</a> "


@app.route("/insert")
def insert():
    user = {'name': "vasya"}
    mongo.db.users.insert(user)
    return "OK"


@app.route("/register")
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = {"name": form.username.data,
            "email": form.email.data,
            "password": "*****"
        }
        return user
    return render_template('templates/register.html', form=form)
    


if __name__ == "__main__":
    app.run(debug=True)


