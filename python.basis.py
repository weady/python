#!/usr/bin/python
#coding: utf-8
#
# by wangdd 2015/12/4

import re
import time
import calendar

def base():
	test = time.localtime(time.time())
	test02 = time.asctime( time.localtime(time.time()) )
	print test
	print test02
	cal = calendar.month(2015,11)
	print cal

	print "Hello world!!"
	#raw_input("Press any key to exit.")
	import sys;x = 'foo';sys.stdout.write(x + '\n')
	a = 23
	b = 10
	c = a - b
	print "value is c",c
	if ( a >b ):
		print "a gt b"
	else:
		print "a lt b"
	if not( a and b ):
	   print "Line 5 - a and b are true"
	else:
	   print "Line 5 - Either a is not true or b is not true"
	if ( b == 10 ) :
		print "OK,The Number is ",a
	else:
		print "Error"
	name = 'wangdong'
	if name == 'wangdong':
		print 'name is',name
	else:
		print 'name is null'
	while b <15:
		print b,'is less than 15'
		b+=1
	else:
		print b,'is more then 15'
		print 'Good bye!'
	for var in 'ABCD':
		print var

	fruits = ['banana', 'apple',  'mango']
	for list in fruits:
		if list=='banana':
			pass
			print "test"
		print list

	print '----------'
	print fruits[1]
	print '----------'
	fruits.append('test')
	print fruits[3]

	print r'\n Good bye!!'

	print "my name is %s ,age is %d" % ('wangdong',28)
	# raw_input 从标准输入读取
	#str = raw_input("Enter one number:");
	#print "your enter number is:",str
	#---------------------------------------------------
	#re.sub 替换命令
	num = "12345 $number"
	phone = re.sub(r'\$.*$','',num)
	print "number is :",phone

	#re.match
	line = "who are you?"
	match = re.match(r'who',line,re.M|re.I)
	search = re.search(r'you\?',line,re.M|re.I)
	#if 多条件用 or and 或 a in list,a not in list
	if match and search :
		print "匹配成功 match:",match.group()
		print "匹配成功 search:",search.group()
	else:
		print "匹配失败 not match"
##############################################################################
#utf-8格式的文件转为gbk格式,原理是函数ReadFile的第二个参数指定以utf-8格式的编码方式读取文件
#返回的结果content为Unicode然后在将Unicode以gbk格式写入文件中
def ReadFile(filePath,encoding="utf-8"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
  
def WriteFile(filePath,u,encoding="gbk"):
    with codecs.open(filePath,"wb") as f:
        f.write(u.encode(encoding,errors="ignore"))
  
def UTF8_2_GBK(src,dst):
    content = ReadFile(src,encoding="utf-8")
    WriteFile(dst,content,encoding="gbk")
##############################################################################
#异常处理
assert False,'error...' 
#先判断assert后面紧跟的语句是True还是False
#如果是True则继续执行print，如果是False则中断程序，调用默认的异常处理器，同时输出assert语句逗号后面的提示信息

def url_character():
	'''开发自用爬虫时,对页面编码进行统一'''
	import chardet
	#抓取网页html
	line = "http://www.pythontab.com"
	html_1 = urllib2.urlopen(line,timeout=120).read()
	encoding_dict = chardet.detect(html_1)
	print encoding
	web_encoding = encoding_dict['encoding']
	#处理，整个html就不会是乱码。
	if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
	html = html_1
	else :
	html = html_1.decode('gbk','ignore').encode('utf-8')

def downloadfile():
	'''下载文件'''

	import urllib2
	import urllib
	import requests

	print "downloading with urllib2"
	url = 'http://www.pythontab.com/test/demo.zip' 
	f = urllib2.urlopen(url) 
	data = f.read() 
	with open("demo2.zip", "wb") as code:     
	    code.write(data)

	# r = requests.get(url) 
	# with open("demo3.zip", "wb") as code:
	# 	code.write(r.content)

	# urllib.urlretrieve(url, "demo.zip")

	

