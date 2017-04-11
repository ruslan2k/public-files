#!/usr/bin/env python

#import commands
import yaml
import numpy as np
import sqlite3
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from subprocess import Popen, PIPE

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
    #print(metric)
    p = Popen((metric['command']).split(), stdout=PIPE)
    output = p.communicate()[0]
    print(p.returncode)
    print(output)


