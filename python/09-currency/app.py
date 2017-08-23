import os
import datetime
import json
import urllib
import urllib.parse
import urllib.request
import pprint as pp

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#pp.pprint(os.environ.get("server"))
DEF_URL = os.environ.get("url")

print(datetime.date.today())

today = datetime.date.today()
month_ago = today - datetime.timedelta(days=30)

print(month_ago.isoformat())

def display(date):
    global url
    url_values = urllib.parse.urlencode({"onDate": date.isoformat(), "Periodicity": 0})
    url = DEF_URL.format(145, url_values)
    pp.pprint(url)
    response = urllib.request.urlopen(url)
    string = response.read().decode("utf-8")
    json_obj = json.loads(string)
    pp.pprint(json_obj["Cur_OfficialRate"])
    pp.pprint(json_obj)


display(month_ago)
display(today)

