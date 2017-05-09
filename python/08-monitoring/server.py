from flask import Flask, redirect, url_for, render_template
import json

app = Flask(__name__)

#app.add_url_rule('/favicon.ico',
#                 redirect_to=url_for('static', filename='favicon.ico'))

@app.route("/")
def index():
    with open("/dev/shm/monitoring/localhost.json", "r") as f:
        data = f.read()
    return render_template('index.html', data=json.loads(data))

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for('static', filename='favicon.ico'), code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

