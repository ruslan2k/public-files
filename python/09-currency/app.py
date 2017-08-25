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
ticker_url = os.environ.get("ticker")

now = datetime.datetime.utcnow()

with urllib.request.urlopen(exchanger_url) as response:
    xml_page = response.read()
root = ET.fromstring(xml_page)

with urllib.request.urlopen(ticker_url) as response:
    ticker_json = response.read()
ticker_data = json.loads(ticker_json.decode())

ticker_last = float(ticker_data["last"])
pp.pprint(ticker_last)

print(root[0].attrib["direction"])
inoutrate = root[1][0].attrib["inoutrate"]
dot_inoutrate = float(re.sub(r",", ".", inoutrate))
#pp.pprint(int(inoutrate))
pp.pprint(dot_inoutrate)

create_q = """ CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY,
    stock STRING,
    inoutrate REAL,
    last REAL,
    created_at DATE
) """

db = sqlite3.connect("db.sq3")
c = db.cursor()
c.execute(create_q)

c.execute("""INSERT INTO history (stock, inoutrate, created_at) VALUES(?,?,?)""", ("wm", dot_inoutrate, now,))
c.execute("""INSERT INTO history (stock, last, created_at) VALUES(?,?,?)""", ("ticker", ticker_last, now,))
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

