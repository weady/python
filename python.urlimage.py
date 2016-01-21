#!/usr/bin/python
#coding=utf8
#获取网页上的图片并保存到本地
import urllib2
import re
req = urllib2.urlopen('http://www.sina.com.cn/')
buf = req.read()
listurl = re.findall(r'http:.+\.jpg',buf)
print listurl
i = 0
for url in listurl:
    f = open(str(i)+'.(jpg|png|gif)','w')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1
