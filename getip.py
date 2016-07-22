#!/usr/bin/env python
# coding=utf-8

import pycurl
import StringIO
import sys

def getlocation(ip):
    b = StringIO.StringIO()
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, "http://freeapi.ipip.net/" + ip)
    curl.setopt(pycurl.USERAGENT, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36")
    curl.setopt(pycurl.WRITEFUNCTION, b.write)

    curl.perform()
    curl.close()

    print(b.getvalue())

def usage():
    print("getip ip")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
        exit()
    getlocation(sys.argv[1])
