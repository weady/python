#!/usr/bin/python
#coding=utf-8

#这个脚本主要作用，利用beautifulsoup 网页解析器进行网页内容的过滤
import re
from bs4 import BeautifulSoup
html_doc="""
 
<p class="title"><b>The Dormouse's story</b></p>
 
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p><span style="font-size:14px;">       </span>
"""

#根据HTML网页字符串创建beautifulsoup 对象
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='uft-8')
#获取URL
links = soup.find_all('a')
for link in links:
	print link.name,link['href'],link.get_text()
#通过正则进行获取
print "-----------------------------------------"
link_node = soup.find('a',href=re.compile(r"els"))
print link_node.name,link_node['href']
p_node = soup.find('p',class_='title')
print p_node.name,p_node.get_text()
