import requests
import json

r = requests.post('http://127.0.0.1:5000/login',
        data=json.dumps({"email":"ruslan", "password":"password"}),
        headers={'content-type': 'application/json'})

authentication_token = r.json()['response']['user']['authentication_token']

print(r.json())

r = requests.get('http://127.0.0.1:5000/a', headers={'content-type': 'application/json'})

print(r)

r = requests.get('http://127.0.0.1:5000/a',
    headers={'authentication-token':authentication_token, 'content-type': 'application/json'})

print(r.json())

