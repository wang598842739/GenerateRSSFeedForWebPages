#coding:UTF-8

import re
import urllib
import rss

#爱羽客见招拆招
c = urllib.urlopen("http://www.aiyuke.com/video_special/254.html").read().decode('utf8')

site = "http://www.aiyuke.com/video_play/"

rss.rssify("aiyuke", site, [{'title': id, 'link':site+id} for (id) in re.findall('<a href="http://www.aiyuke.com/video_play/(.*?)">', c)])
