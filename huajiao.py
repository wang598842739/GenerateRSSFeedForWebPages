#!/usr/bin/python

import re, urllib
import rss

c = urllib.urlopen("http://www.huajiao.com/category/1000").read().decode('utf8')

site = "http://www.huajiao.com/l/"

rss.rssify("huajiao", site, [{'title': id, 'link':site+id} for (id) in re.findall('<a href="/l/(.*?)">', c)])
