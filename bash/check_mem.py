#!/usr/bin/env python

import psutil
import pprint as pp

DEF_ELEM = 3
user_dict = {}
all_mem = 0

for pid in psutil.pids():
    p = psutil.Process(pid)
    all_mem += p.memory_info().rss
    username = p.username()
    if username in user_dict:
        user_dict[username]["rss_sum"] += p.memory_info().rss
    else:
        user_dict[username] = {}
        user_dict[username]["rss_sum"] = p.memory_info().rss
#pp.pprint(user_dict)

rss_dict = {mem["rss_sum"]:user for user,mem in list(user_dict.items())}
max_rss = ({rss:rss_dict[rss] for rss in sorted(rss_dict,reverse=True)[0:DEF_ELEM]})

#pp.pprint(rss_dict)
#pp.pprint(max_rss)
mem_str = "OK - all rss {0} |all_users={0}".format(all_mem)
sss = ";;; ".join("{}={}".format(u, m) for m, u in max_rss.items())
print("{0};;; {1}".format(mem_str, sss))
