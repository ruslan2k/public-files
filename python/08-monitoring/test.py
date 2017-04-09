#!/usr/bin/env python

import yaml
import numpy as np
import sqlite3
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


f_name = "/tmp/a.png"

t = np.arange(0., 10., 0.1)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.plot(t, t, 'r--', t, t**2, 'bs')
plt.savefig(f_name)

with open("config.yml", "r") as f:
    config = yaml.load(f)

for metric in config:
    print(metric)
