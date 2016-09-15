#!/usr/bin/env python

import psutil
import pprint as pp

user_dict = {}
all_mem = 0

for pid in psutil.pids():
    p = psutil.Process(pid)
    all_mem += p.memory_percent()
    username = p.username()
    if username in user_dict:
        user_dict[username]["rss_sum"] += p.memory_info().rss
    else:
        user_dict[username] = {}
        user_dict[username]["rss_sum"] = p.memory_info().rss
    print(p.username())
    print(p.memory_percent())
    print(p.memory_info())

pp.pprint(user_dict)

sorted(user_dict, key=lambda x: x["rss_sum"])

#print("all mem: {0}".format(all_mem))

    
