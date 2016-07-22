#!/usr/bin/env python
# coding=utf-8

import sys
import StringIO
import urllib2
import json

apikey = "9ff61ed5ed053e76c5d1c73794fe1073"

class C():
    def __init__(this):
        this.api = {'we': {'url': 'http://apis.baidu.com/heweather/pro/weather', 'function': this.getweather}, 
                }

    def getweather(this, cnt, city):
        req = urllib2.Request(this.api[cnt]['url'] + "?city=" + city)
        req.add_header('apikey', apikey)

        resp = urllib2.urlopen(req)
        jsonstr = resp.read()
        print(jsonstr)
        


def usage():
    print("Usage: tools cnt para\n")
    print("cnt:")
    print("we for weather, needs parameter cityname")


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        usage()
        exit()
    c = C()
    if c.api.has_key(sys.argv[1]):
        c.api[sys.argv[1]]['function'](sys.argv[1], sys.argv[2])
