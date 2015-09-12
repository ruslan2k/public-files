#!/usr/bin/env python


from functools import wraps
from flask import Flask, request, Response


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
        # FIXME


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world<br>" \
        + "<a href='http://flask.pocoo.org/snippets/8/'>doc</a>"
    

if __name__ == "__main__":
    app.run(debug=True)


