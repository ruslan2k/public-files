import os
import re
import datetime
import json
import urllib
import urllib.parse
import urllib.request
import pprint as pp
import sqlite3
import xml.etree.ElementTree as ET

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DEF_URL = os.environ.get("url")
exchanger_url = os.environ.get("exchanger")

now = datetime.datetime.utcnow()

with urllib.request.urlopen(exchanger_url) as response:
    xml_page = response.read()

root = ET.fromstring(xml_page)

print(root[0].attrib["direction"])
inoutrate = root[1][0].attrib["inoutrate"]
dot_inoutrate = float(re.sub(r",", ".", inoutrate))
#pp.pprint(int(inoutrate))
pp.pprint(dot_inoutrate)

db = sqlite3.connect("db.sq3")
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, inoutrate REAL, created_at DATE)""")

c.execute("""INSERT INTO history (inoutrate, created_at) VALUES(?,?)""", (dot_inoutrate, now,))
db.commit()

db.close()

#print(datetime.date.today())
#
#today = datetime.date.today()
#month_ago = today - datetime.timedelta(days=30)
#
#print(month_ago.isoformat())
#
#def display(date):
#    global url
#    url_values = urllib.parse.urlencode({"onDate": date.isoformat(), "Periodicity": 0})
#    url = DEF_URL.format(145, url_values)
#    pp.pprint(url)
#    response = urllib.request.urlopen(url)
#    string = response.read().decode("utf-8")
#    json_obj = json.loads(string)
#    pp.pprint(json_obj["Cur_OfficialRate"])
#    pp.pprint(json_obj)
#
#
#display(month_ago)
#display(today)

