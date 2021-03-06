import requests
import json

r = requests.post('http://127.0.0.1:5000/register',
        data=json.dumps({"email":"ruslan@example.com", "password":"password"}),
        headers={'content-type': 'application/json'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/login',
        data=json.dumps({"email":"ruslan@example.com", "password":"password"}),
        headers={'content-type': 'application/json'})

print(r.text)
authentication_token = r.json()['response']['user']['authentication_token']
print(r.json())

r = requests.get('http://127.0.0.1:5000/a',
        headers={'content-type': 'application/json'})
print(r.text)

r = requests.get('http://127.0.0.1:5000/a',
    headers={'authentication-token':authentication_token, 'content-type': 'application/json'})
print(r.json())

r = requests.get('http://localhost:5000/d/is-online/mac/12:34-56')
print(r.json())

r = requests.post('http://localhost:5000/c',
        data=json.dumps({'mac':'00:00:00', 'name':'Test'}),
        headers={'authentication-token':authentication_token, 'content-type': 'application/json'})
#print(r.text)
print(r.json())

r = requests.get('http://localhost:5000/c',
        headers={'authentication-token':authentication_token, 'content-type': 'application/json'})
print(r.json())

