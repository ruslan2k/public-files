import json

import flask
import requests
import pprint


from config import CLIENT_ID, CLIENT_SECRET 

app = flask.Flask(__name__)

#SCOPE = 'https://www.googleapis.com/auth/drive.metadata.readonly'
SCOPE = 'https://www.googleapis.com/auth/plus.login'
SCOPE = 'https://www.googleapis.com/auth/plus.me'
SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
SCOPE = 'email profile'
REDIRECT_URI = 'http://home.jkl.su:5000/oauth2callback'


@app.route('/')
def index():
  if 'credentials' not in flask.session:
    return flask.redirect(flask.url_for('oauth2callback'))
  credentials = json.loads(flask.session['credentials'])
  if credentials['expires_in'] <= 0:
    return flask.redirect(flask.url_for('oauth2callback'))
  else:
    headers = {'Authorization': 'Bearer {}'.format(credentials['access_token'])}
    req_uri = 'https://www.googleapis.com/drive/v2/files'
    req_uri = 'https://www.googleapis.com/userinfo/email'
    print(req_uri)
    r = requests.get(req_uri, headers=headers)
    print()
    print(r.text)
    print()
    pprint.pprint(vars(r))
    #return r.text
    resp = '<a href="https://accounts.google.com/o/oauth2/revoke?token={token}">log out</a>'.format(token=credentials['access_token'])
    return resp #+ vars(r)


@app.route('/oauth2callback')
def oauth2callback():
  if 'code' not in flask.request.args:
    auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
    return flask.redirect(auth_uri)
  else:
    auth_code = flask.request.args.get('code')
    data = {'code': auth_code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'}
    r = requests.post('https://www.googleapis.com/oauth2/v4/token', data=data)
    flask.session['credentials'] = r.text
    return flask.redirect(flask.url_for('index'))


if __name__ == '__main__':
  import uuid
  app.secret_key = str(uuid.uuid4())
  app.debug = True
  app.run(host='0.0.0.0')
