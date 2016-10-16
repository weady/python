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

##############################################################################
#这个笔记主要记录<python网络编程攻略>的学习笔记

#------------------第一章---------------------------------
def part1():
	print "-"*30 +'第一章开始' + "-"*30

	import socket
	from binascii import hexlify  #以十六进制形式表示二进制数据

	host = socket.gethostname()	#获取主机名
	print "主机名 =>  %s " % host
	print "主机IP =>  %s " % socket.gethostbyname(host) #获取主机名对应的IP

	remote_host = 'www.baidu.com'
	try:
		print "远程主机www.baidu.com的IP => %s " % socket.gethostbyname(remote_host)
	except socket.error,err_msg:
		print err_msg

	'''
	python的socket库提供了很多用来处理不同IP地址格式的函数,inet_aton()和 inet_ntoa()
	inet_aton()将一个字符串IP地址转换为一个32位的网络序列IP地址。
	aton 就是ascii string to numberic ，把字符串转成数据
	inet_ntoa()正好相反，把IP数据转换成字符串
	socket.inet_aton(ip_string) 转换IPV4地址字符串（192.168.10.8）成为32位打包的二进制格式
	（长度为4个字节的二进制字符串）它不支持IPV6。inet_pton()支持IPV4/IPV6地址格式
	socket.inet_ntoa(packed_ip) 转换32位打包的IPV4地址为IP地址的标准点号分隔字符串表示
	'''
	for ip_addr in ['127.0.0.1','192.168.1.1']:
		packed_ip_addr = socket.inet_aton(ip_addr)
		unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)

		print "IP Address: %s => Packed: %s,Unpacked: %s " % (ip_addr,hexlify(packed_ip_addr),unpacked_ip_addr)

	'''
	通过指定的端口和协议找到服务名 socket.getservbyport() 函数来获取服务的名字
	'''
	protocalname = 'tcp'

	for port in [25,80,22,53,110,443]:
		print "Port: %s = > service name: %s" % (port,socket.getservbyport(port,protocalname))

	print "Port: %s = > service name: %s" % (53,socket.getservbyport(53,'udp'))

	'''
	编写底层网络应用时,或许利用电缆在两台设备之间传送底层数据,在这种操作中需要把主机操作系统发出的数据转换为网络格式
	或者逆向转换,利用socket模块中的ntohl()和htonl() n 表示网络 h 表示主机 l 表示长整形 s 表示短整形 即16位
	'''
	data = 123456
	#32-bit
	print "[32-bit] Original:%s => Long host byte order: %s,Network byte order:%s" \
		% (data,socket.ntohl(data),socket.htonl(data))
	#16-bit
	print "[16-bit] Original:%s => Short host byte order: %s,Network byte order:%s" \
		% (data,socket.ntohs(data),socket.htons(data))

	'''
	套接字超时时间,利用gettiimeout()获取默认的超时时间调用settimeout() 方法设定一个超时时间
	传给settimeout()方法的参数可以是秒数(非负浮点数),也可以是None.这个方法在处理阻塞式套接字操作时使用
	如果把超时时间设置为None，则为禁用了套接字操作的超时检测
	'''
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "Default socket timeout: %s " % s.gettimeout()
	s.settimeout(100)
	print "Current socket timeout: %s " % s.gettimeout()
	
	'''
	python 的socket库提供了一个方法，能通过socket.error异常优雅地处理套接字错误
	默认的套接字缓冲区大小可能不够用，可以利用setsockopt()方法修改默认的套接字缓冲区大小
	常用的两个变量:SEND_BUF_SIEZ RECV_BUF_SIZE
	在套接字对象上可调用getsockopt()和setsockopt()分别获取和修改套接字对象的属性
	setsockopt()方法接收三个参数level,optname(选项名),value(具体的值)
	'''
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	SEND_BUG_SIZE = 4096
	RECV_BUF_SIZE = 4096

	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF) #获取默认的发送缓冲区大小
	print "Buffer size [Before]:%d" % bufsize

	sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_SNDBUF,
		SEND_BUG_SIZE
		)
	sock.setsockopt(
		socket.SOL_SOCKET,
		socket.SO_RCVBUF,
		RECV_BUF_SIZE
		)
	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print "Buffer size [After]:%d" % bufsize

	'''
	默认情况下,TCP套接字处于阻塞模式中，除非完成了某项操作，否则不会把控制权交给程序
	在非阻塞模式下,如果遇到问题就会抛出异常，在阻塞模式下遇到错误并不会阻止操作
	利用setblocking(1)--阻塞模式 和setblocking(0)--非阻塞模式
	'''
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setblocking(1)
	s.settimeout(0.5)
	s.bind(('127.0.0.1',0))

	socket_address = s.getsockname()

	print "Trivial Server lanunched on socket:%s" %str(socket_address)
	# while 1:
	# 	s.listen(1)

	'''
	重用套接字地址,先查询地址重用的状态，调用setsockopt()方法,修改地址重用状态的值,再按照常规的步骤
	把套接字绑定一个地址上,监听进入的客户端连接
	'''
	def reuse_socket_addr():
		import socket
		import sys
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
		print "Old sock state:%s" % old_state

		sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
		print "New sock state:%s" %new_state

		local_port = 8282

		srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		srv.bind(('',local_port))
		srv.listen(1)
		print "Listening on port:%s" % local_port
		while  True:
			try:
				connnection,addr = srv.accept()
				print 'Connected by %s:%s' % (addr[0],addr[1])
			except KeyboardInterrupt:
				break
			except socket.error,msg:
				print '%s' % msg

	'''
	利用ntplib 模块同步时间
	'''
	import ntplib
	import time

	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	print "Current time is %s " % time.ctime(response.tx_time)

	print "-"*30 +'第一章结束' + "-"*30

def part2():
	print "-"*30 +'第二章开始' + "-"*30

	import socket
	import os
	import threading
	import SocketServer

	'''
	SocketServer 模块提供了两个实用类:ForkingMixIn 和 ThreadingMinxIn ForkingMixIn会为每个客户端请求派生一个新进程
	服务器处理客户端发出的请求时不能阻塞,因此要找到一种机制来单独处理每个客户端
	'''
	SERVER_HOST = '127.0.0.1'
	SERVER_PORT = 0 #随机选择一个端口
	BUF_SIZE = 1024
	ECHO_MSG = 'Hello echo server!'

	class ForkingClient():
	    def __init__(self,ip,port):
	            self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	            self.sock.connect((ip,port))

	    def run(self):
	        current_process_id = os.getpid()
	        print "PID %s Sending echo message to the server :%s " % (current_process_id,ECHO_MSG)
	        sent_data_length = self.sock.send(ECHO_MSG)
	        print "Sent:%d characters,so far..." % sent_data_length

	        response = self.sock.recv(BUF_SIZE)
	        print "PID %s received:%s " % (current_process_id,response[5:])

	    def shutdown(self):
	    	self.sock.close()

	class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):

		"""docstring for ForkingServerRequestHandler"""
		def handle(self):
			data = self.request.recv(BUF_SIZE)
			current_process_id = os.getpid()
			response = '%s :%s ' % (current_process_id,data)

			print "Server sending response [current_process_id:data] = [%s]" % response.self.request.send(response)
			return
	class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer):		
			pass
	
	def main():
		server = ForkingServer((SERVER_HOST,SERVER_PORT), ForkingServerRequestHandler)
		ip,port = server.server_address
		server_thread = threading.Thread(target=server.serve_forever)
		server_thread.setDaemon(True)
		server_thread.start()
		print 'Server loop running PID:%s' % os.getpid()

		client1 = ForkingClient(ip, port)
		client1.run()

		client2 = ForkingClient(ip, port)
		client2.run()

		server.shutdown()
		client1.shutdown()
		client2.shutdown()
		server.socket.close()


	print "-"*30 +'第二章结束' + "-"*30

	print id('111111')
	print id(111111)
	print divmod(1, 4)
	print range(1,10)

	print eval(1+3)















