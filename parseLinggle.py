#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib2
import json
import re


def parselinggle(itemlist):
    #itemlist : a list of words
    itemlist = [v for v in itemlist if v]
    #you'd better use the %20 to fill the blank between the word or it may occur an error!
    token = "%20".join(itemlist)
    # insert sapce or not is the same!
    page = urllib2.urlopen(u'http://www.linggle.com/query/%s' %token,timeout=1000)
    if page.getcode()==200:
        result = json.loads(page.read())
        if not result:
            return 0
        else:
            return result[0]["count"]
    else:
        return 0

if __name__ == "__main__":
    parselinggle(['resource','HR'])
