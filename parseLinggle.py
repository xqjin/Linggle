#!/usr/bin/python
#-*- coding:utf-8 -*-
import random
import pickle
import re
import sys
import os
import urllib
import json
import configure
import parseNumTree as pnt
from stemming.porter2 import stem
from Key2Value import PrepKV as PKV
from Key2Value import ArtKV as AKV
from Key2Value import NnKV as NKV
from nltk.corpus import cmudict as cmu
from nltk.corpus import wordnet as wn
from Arpabet import isAorAn
from UCN import UCN
import nltk


def parselinggle(itemlist):
    #token = "%20".join(itemlist)
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