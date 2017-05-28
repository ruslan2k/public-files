#!env python

import glob
import re
import os
import urllib2
import logging

DEF_FEEDS = [
    {"dir": "deflope", "rss": "http://feeds.feedburner.com/devopsdeflope"},
    {"dir": "pirates", "rss": "http://feeds.feedburner.com/pirate-radio-t"},
    {"dir": "radio-t", "rss": "http://feeds.rucast.net/radio-t"},
    {"dir": "umputun", "rss": "http://feeds.rucast.net/umputun"},
]

def downloadSplitRm(url, fdir, file_name):
    wget_cmd='wget -c --directory-prefix={} {}'.format(fdir, url)
    splt_cmd='cd %s && mp3splt -t 10.00 -o @f.@m-@M %s' %(fdir, file_name)
    logging.warning("Cmd: %s"% wget_cmd)
    logging.warning("Cmd: %s"% splt_cmd)
    os.system(wget_cmd)
    os.system(splt_cmd)
    os.remove(os.path.join(fdir, file_name))

def download(feed):
    fdir=feed["dir"]
    rss=feed["rss"]
    last_index = 0
    logging.warning("rss: {}".format(rss))
    mp3s = glob.glob(fdir + "/*.mp3")
    if mp3s:
        max_mp3 = max(mp3s)
        m2 = re.match(r"[^0-9]*(\d+).*\.mp3", max_mp3)
        last_index = m2.group(1)
    logging.warning("last_index: {}".format(last_index))
    response = urllib2.urlopen(rss)
    xml = response.read()
    pattern = r'(http[^<>\'"=]+\.mp3)'
    lst = re.findall(pattern, xml)
    mp3_set = sorted(set(lst))     # make uniq
    for url in mp3_set:
        m1 = re.match(r".+[/](\D+(\d+).*\.mp3)", url)
        file_name = m1.group(1)
        number = m1.group(2)
        if number > last_index:
            logging.warning(url)
            downloadSplitRm(url, fdir, file_name)

if __name__ == "__main__":
    list(map(download, DEF_FEEDS))

