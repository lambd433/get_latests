#!/usr/bin/env python3.4

#
# Usage: ./get_latests.py [-s splitter] [-v] url [item-name.ext]
#

#import requests
import urllib.request
import re
import sys
import argparse

splitter = '-'
item2n_ve = r"(?P<name>(.*)){splitter}(?P<ver_ext>(.*))$"
ve2v_e = r"(?P<ver>((\d+)((\.(\d+))*)))(?P<ext>(.*))"
ne2n_e = r"^(?P<name>[^\.]*)(?P<ext>\..*)$"
item_def = r"<a href=\"(?P<item_url>\S+)\">(?P<item_name>\S+)</a>"

def get_info(item):
    nve = re.match(item2n_ve.format(splitter=splitter), item)
    if nve:
        ver_ext = nve.group('ver_ext')
        ve = re.match(ve2v_e, ver_ext)
        if ve: # with extension
            return (nve.group('name'), ve.group('ver'), ve.group('ext'))
        else: # no extension
            return (nve.group('name'), '', '')
def get_latests(html):
    a = re.findall(item_def, html)
    latests = dict()
    for _ui, i in a:
        res = get_info(i)
        if res:
            n, v, e = res
            if latests.get((n, e), '0') < v:
                latests[(n, e)] = v

    return latests

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--splitter')
    parser.add_argument('-v', '--version', action='store_true', default=False)
    parser.add_argument('url')
    parser.add_argument('name_ext', nargs='?', default=False)
    args = parser.parse_args()
 
# For requests        
    # r = requests.get(url)
    # base_url = r.url
    # html = r.text

# For urllib2
    r = urllib.request.urlopen(args.url)
    base_url = r.geturl()
    html = str(r.read())

    if args.name_ext:
        ne = re.match(ne2n_e, args.name_ext)
        name = ne.group('name')
        ext = ne.group('ext')
        latests = get_latests(html)
        for ne, v in latests.items():
            n, e = ne
            if n==name and e==ext:
                if args.version:
                    print(v)
                else:
                    print(base_url+n+args.splitter+v+e)

    else:
        latests = get_latests(html)
        for ne, v in latests.items():
            n, e = ne
            print(base_url+n+args.splitter+v+e)
