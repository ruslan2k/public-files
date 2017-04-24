#!/usr/bin/env python

import os
import json
import yaml
import numpy as np
import sqlite3
import socket
import time
from pprint import pprint
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import subprocess

f_name = "/tmp/a.png"
shm_dir = "/dev/shm/monitoring"

if not os.path.exists(shm_dir):
    os.makedirs(shm_dir)

t = np.arange(0., 10., 0.1)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.plot(t, t, 'r--', t, t**2, 'bs')
plt.savefig(f_name)

conn = sqlite3.connect('monitoring.sq3')
c = conn.cursor()

with open("config.yml", "r") as f:
    config = yaml.load(f)
metrics = config['checks']

for metric in metrics:
    c.execute("""
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY ASC, 
        time timestamp default (strftime('%s', 'now')),
        value text )""".format(metric['name']))
    conn.commit()

checks = []
for metric in metrics:
    output = {}
    output['name'] = metric['name']
    p = subprocess.Popen((metric['command']).split(),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    output['ret_code'] = p.returncode
    output['stdout'] = "".join(out.decode("utf-8"))
    output_data = (out.decode('utf-8').split('|')[1]).strip()
    sql = " INSERT INTO {} values(NULL, ?, ?) ".format(metric['name'])
    c.execute(sql, (int(time.time()), output_data))
    conn.commit()
    checks.append(output)

status = {
    "hostname": socket.gethostname(),
    "timestamp": int(time.time()),
    "checks": checks,
}

# pprint(status)
with open(shm_dir +"/localhost.json", "w") as outfile:
    json.dump(status, outfile)

