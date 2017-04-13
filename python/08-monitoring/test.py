#!/usr/bin/env python

import yaml
import numpy as np
import sqlite3
import time
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import subprocess

f_name = "/tmp/a.png"

t = np.arange(0., 10., 0.1)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.plot(t, t, 'r--', t, t**2, 'bs')
plt.savefig(f_name)

conn = sqlite3.connect('monitoring.sq3')
c = conn.cursor()

with open("config.yml", "r") as f:
    config = yaml.load(f)

for metric in config:
    c.execute("""
        CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY ASC, 
        time timestamp default (strftime('%s', 'now')),
        value text )""".format(metric['name']))
    conn.commit()

for metric in config:
    print(metric['name'])
    p = subprocess.Popen((metric['command']).split(),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(p.returncode)
    output_data = (out.decode('utf-8').split('|')[1]).strip()
    print(out.decode('utf-8').split('|'))
    sql = " INSERT INTO {} values(NULL, ?, ?) ".format(metric['name'])
    print(sql)
    c.execute(sql, (int(time.time()), output_data))
    conn.commit()
    



