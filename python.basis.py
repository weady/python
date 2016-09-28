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

##############################################################################
#经典的冒泡 选择 插入排序算法
def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(i,len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] = tmp
                  
def selection_sort(seq):
    for i in range(len(seq)):
        position = i
        for j in range(i,len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
                tmp = seq[position]
                seq[position] = seq[i]
                seq[i] = tmp
  
def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1,len(seq)):
            while i > 0 and seq[i] < seq[i-1]:
                tmp = seq[i]
                seq[i] = seq[i-1]
                seq[i-1] = tmp
                i = i - 1

##############################################################################
#发生器 yield
import sys

def read_file(fpath): #通过发生器读取文件,减少对内存的占用
   BLOCK_SIZE =1024
   with open(fpath, 'rb') as f:
       while True:
           block =f.read(BLOCK_SIZE)
           if block:
               yield block
           else:
               return

filename = sys.argv[1]

for i in read_file(filename):
        print i 

##############################################################################
#一个使用了多线程处理的服务器示例
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
#定义支持多线程的服务类，注意是多继承
class Server(ThreadingMixIn, TCPServer):
	pass
#定义请求处理类
class Handler(StreamRequestHandler)：
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from ',addr
		self.wfile.write('Thank you for connection')
		server = Server(('', 1234), Handler)#实例化服务类
		server.serve_forever()#开启服务

##############################################################################
#解决中文乱码的函数 
def deal_char():
	s="中文"
	if isinstance(s, unicode): 
	    #s=u"中文"  
	    print s.encode('gb2312') 
	else: 
	    #s="中文"  
	    print s.decode('utf-8').encode('gb2312')

##############################################################################
#异常处理方式
#1.try execpt
	try:
		pass
	except Exception as e:
		print Exception,":",e 
#2.采用traceback模块
	import traceback
	try:
		pass
	except:
		traceback.print.exc()

	#把异常写入到文件中
	try:
		pass
	except:
		f=open('text.log','a')
		traceback.print_exc(file=f)
		f.flush()
		f.close()
#3.采用sys模块回溯最后的异常
	import sys
	try:
		pass
	except:
		info = sys.exc_info()
		print info[0],":",info[1]


















