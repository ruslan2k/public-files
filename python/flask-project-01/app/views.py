from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ruslan'}    # user
    groups = ['Unix', 'Windows', 'QA']
    return render_template("index.html", title = 'Home', user = user, groups = groups)




