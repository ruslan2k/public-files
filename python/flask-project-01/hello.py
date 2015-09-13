#!/usr/bin/env python


from functools import wraps
from flask import Flask, request, Response
from flask.ext.pymongo import PyMongo

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
    users = mongo.db.users.find({'online': True})
    print users
    return "Hello world<br>" \
        + "<a href='http://flask.pocoo.org/snippets/8/'>doc</a>"
    

if __name__ == "__main__":
    app.run(debug=True)


