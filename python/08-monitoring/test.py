#!/usr/bin/env python

import os
import yaml
import numpy as np
import sqlite3
import time
import pprint as pp
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import subprocess

f_name = "/tmp/a.png"
shm_dir = "/dev/shm/monitoring"
client_dir = shm_dir +"/client"

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
checks = config['checks']

for metric in checks:
    c.execute("""
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY ASC, 
        time timestamp default (strftime('%s', 'now')),
        value text )""".format(metric['name']))
    conn.commit()

for metric in checks:
    output = {}
    output['name'] = metric['name']
    p = subprocess.Popen((metric['command']).split(),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    output['ret_code'] = p.returncode
    output['stdout'] = out.decode('utf-8')
    output_data = (out.decode('utf-8').split('|')[1]).strip()
    sql = " INSERT INTO {} values(NULL, ?, ?) ".format(metric['name'])
    c.execute(sql, (int(time.time()), output_data))
    conn.commit()
    pp.pprint(output)
    



