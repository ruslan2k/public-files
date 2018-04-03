from functools import wraps
from pprint import pprint
from flask import Flask, g

app = Flask(__name__)


def debug_info(a, b):
    #@wraps(f)
    pprint((g))
    def decorated_function(*args, **kwargs):
        pprint("args")
        pprint(args)
        pprint("kwargs")
        pprint(kwargs)
        return "OK"
        #return f(*args, **kwargs)
    return decorated_function
        

@debug_info("a", "b")
@app.route("/")
def hello_world():
    return "Hello, World!"

