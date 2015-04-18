#!/usr/bin/python
#-*- coding:utf-8 -*-
import urllib
import json



def parselinggle(itemlist):
    #itemlist : a list of words
    token = " ".join(itemlist)
    # insert sapce or not is the same!
    page = urllib.urlopen(u'http://www.linggle.com/query/%s' %token)
    if page.getcode()==404:
        return 0

    result = json.loads(page.read())
    if not result:
        return 0
    else:
        return result[0]["count"]
