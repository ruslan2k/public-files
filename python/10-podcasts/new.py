#!env python3

import os
import pprint
import re
import urllib.request
import yaml


def main():
    with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    list(map(process_podcast, cfg["podcasts"]))


def process_podcast(podcast):
    pprint.pprint(podcast)
    fees_name = podcast["name"]
    url = podcast["url"]
    print(fees_name)
    response = urllib.request.urlopen(url)
    text = response.read().decode("latin-1")
    p = re.compile('http://[^"]+\.mp3')
    m = p.findall(text)
    mp3s = set(m)
    for mp3_url in mp3s:
        m1 = re.match(r".+[/](.+\.mp3)", mp3_url)
        print(m1.group(1), mp3_url)
        wget_cmd='wget -c --directory-prefix={} {}'.format(fees_name, mp3_url)
        os.system(wget_cmd)


def download(url_mp3, file_mp3):
    urllib.request.urlretrieve(url_mp3, file_mp3)


if __name__ == "__main__":
    main()

