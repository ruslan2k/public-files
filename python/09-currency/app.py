import os
import re
import datetime
import json
import urllib
import urllib.parse
import urllib.request
import pprint as pp
import xml.etree.ElementTree as ET

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#pp.pprint(os.environ.get("server"))
DEF_URL = os.environ.get("url")
exchanger_url = os.environ.get("exchanger")

with urllib.request.urlopen(exchanger_url) as response:
    xml_page = response.read()

#pp.pprint(xml_page)
root = ET.fromstring(xml_page)

#pp.pprint(root[1][0].tag)
#pp.pprint(root[1][0].attrib)
#pp.pprint(root[1][0].attrib["inoutrate"])
print(root[0].attrib["direction"])
inoutrate = root[1][0].attrib["inoutrate"]
dot_inoutrate = re.sub(r",", ".", inoutrate)
#pp.pprint(int(inoutrate))
pp.pprint(float(dot_inoutrate))

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

