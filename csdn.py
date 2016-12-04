#!/usr/bin/python

import re, urllib
import rss

c = urllib.urlopen("http://www.qtfy30.cn/ysyl").read().decode('utf8')

site = "http://www.qtfy30.cn/ysyl/"

rss.rssify("qietingfengyin", site, [{'title': t, 'link':site+l} for (l,t) in re.findall('"><a href="(.*?)">(.*?)</a>', c)])
