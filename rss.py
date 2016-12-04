#!/sw/bin/python

import urllib, re, os

import sys

titlere = re.compile("<TITLE>(.*?)</TITLE>", re.I|re.S)
def gettitle(c):
	x = titlere.findall(c)
	if x: return x[0]
	return None

def htmlencode(text):
	return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def rssify(title, link, items, encoding='utf8'):
	if os.environ.has_key("QUERY_STRING"):
		print "Content-Type: application/xml; charset="+encoding
		print	
	if encoding != 'utf8':
		print '<?xml version="1.0" encoding="'+encoding+'"?>'
	print '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel>\n  <title>'+htmlencode(title)+'</title>\n  <link>' + htmlencode(link) + '</link>\n  <description>'+"Scraped feed provided by aaronsw.com"+'</description>'
	for item in items:
		print "  <item>"
		if type(item) is not type({}): item = {'description': item}
		x = item.keys(); x.sort()
		for k in x:
			print "    <"+k+">" + htmlencode(item[k]) + "</"+k+">"
		print "  </item>"
	print "</channel></rss>"

def fromurl(url, title=None):
	content = urllib.urlopen(url).read()
	
	if title:
		x = gettitle(content)
		if x: content = {'title': x, 'description': content, 'link':url}
	else: title = gettitle(content)

	return rssify(title, url, [content])
	
def fromlist(title, link, itemlist):
	items = []
	for l in itemlist:
		content = urllib.urlopen(l).read()
		ntitle = gettitle(content)
		
		if ntitle: items.append({'title': ntitle, 'description': content, 'link':l})
		else: items.append(content)

	return rssify(title, link, items)

# fromurl("http://vitanuova.loyalty.org/latest.html", "Vitanuova")
# Rys, Zooko: custom regexp
# Lawmeme, Politech: fromlist
# Mena, Mark's Projects: email owners
# http://www.sfgate.com/examiner/bondage/ http://dir.salon.com/topics/tom_tomorrow/ (use jwz's feed?)
# check on true porn clerk stories, mixerman
