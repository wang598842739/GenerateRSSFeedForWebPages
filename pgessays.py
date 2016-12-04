#!/usr/bin/python

import re, urllib
import rss

c = urllib.urlopen("http://www.paulgraham.com/articles.html").read()

site = "http://www.paulgraham.com/"
rss.rssify("Paul Graham: Essays", site, [{'title': t, 'link':site+l} for (l,t) in re.findall('"><a href="(.*?)">(.*?)</a>', c)])
