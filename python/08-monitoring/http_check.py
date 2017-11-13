import os
import requests
from config import *

response = requests.get(url, auth=(auth_user, auth_pass))
print(response.status_code)

if (response.status_code == 200) or os.path.isfile('http.lock'):
    exit()


