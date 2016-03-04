#!/usr/bin/python
#coding:utf-8
#
#这个文件中主要是对基本模块功能介绍
#
#	by wangdd 2016/02/19
#
#画图的类库 canvas
from reportlab.pdfgen import canvas
#用于定位的inch库,inch将作为我们的高度宽度的单位
from reportlab.lib.units import inch
import subprocess
import datetime
import os

#---------------------01-------------------------------------
#subprocess 模块可以用于执行shell命令
def sub_mode():
    #command 1
    uname = "uname"
    uname_args = "-a"
    subprocess.call([uname,uname_args])
    #command 2
    diskspace = "df -lh"
    disk = subprocess.Popen(diskspace,shell=True,stdout=subprocess.PIPE)
    return disk.stdout.readlines()
#----------------------02--------00--------------------------
#reportlab 模块,用于把数据格式化成PDF类型的文件
def hello():
    c = canvas.Canvas('test.pdf')
    c.drawString(100,100,'hello world')
    c.showPage()
    c.save()

#canvas 用于创建一个画布;textobject创建一个放在pdf中的对象,inch是pdf的文件大小;textLines 是文件中每行的内容
#drawText 
def disk_status(input,output="disk_status.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h %d %Y %H:%M:%S")
    #声明canvas类对象,传入的就是生成的pdf文件名字
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch,11*inch)
    textobject.textLines(''' Disk Capacity Report:%s''' % date)
    for line in input:
	textobject.textLine(line.strip())
    #写入内容到pdf文件中
    c.drawText(textobject)
    ##showpage将保留之前的操作内容之后新建一张空白页
    c.showPage()
    #将所有的页内容存到打开的pdf文件里面
    c.save()

#report = sub_mode()
#disk_status(report)
    
#----------------------03------------------------------------
#socket 网络通信编程,最简单的网络通信模型代码
import socket
#server 端 
def socket_server():
	host = '192.168.36.130'
	port = 51000

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,port))

	s.listen(1)
	conn,addr = s.accept()

	print 'Conneted by',addr
	while 1:
        	data = conn.recv(1024)
        	if not data:
                	break
        	conn.sendall(data)
	conn.close()

#clent 端
def socket_client():
	host = '192.168.36.130'
	port = 51000

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))

	s.sendall('Hello,world')
	data = s.recv(1024)
	s.close()
	print 'Received',data
#----------------------04------------------------------------
#利用psutil 模块获取进程的相关信息
import psutil
def get_process_info():
    for pid in psutil.pids():
	if pid == 1 or pid == 2:
		continue
	else:
		p = psutil.Process(pid)
		print "进程名:",p.name() +'\t'"进程bin路径:",p.exe() +'\t' "进程工作目录:",p.cwd() \
		+'\t' "进程状态:",p.status() +'\t' "进程CPU时间信息:",p.cpu_times() \
		#+'\t' "socket 信息:",str(p.connections())
		#+'\t' "进程实际消耗内存值:", p.memory_info().rss +'\t' "进程开启的线程数:",p.num_threads()
#get_process_info()

#----------------------05------------------------------------
#IPy 模块进行IP地址的规划
from IPy import IP
def contral_ips():
	ip_version = IP('10.0.0.1').version()
	ip_list =[]
	print "IP 版本:%s" % ip_version
	print IP('8.8.8.8').reverseNames()	#反向解析地址格式

	ip_s = raw_input("请输入IP地址或网络地址(eg:192.168.1.0/24):")
	ips = IP(ip_s)
	for ip in ips:
		ip_list.append(ip)	#打印出192.168.1.0/16网段的所有IP清单
	print "IP地址范围:",ip_list

	if len(ips)>1:	#为一个网络地址
		print 'net: %s' % ips.net()
		print 'netmask: %s' % ips.netmask()
		print 'broadcast: %s' % ips.broadcast()
		print 'reverse address: %s' % ips.reverseNames()[0]
		print 'subnet: %s' % len(ips)
	else:
		print 'reverse address: %s' % ips.reverseNames()[0]
	
#----------------------06------------------------------------
#dnspython ,python实现的一个DNS工具包，可以替代nslookup,dig等工具
#dnspython 提供了一个nds解析器类 resolver,使用它的query方法实现域名的查询功能
import dns.resolver
def dns_resolver():
   domain = raw_input("输入域名:")		#输入域名地址
   A = dns.resolver.query(domain,'A')	#查询A记录
   MX = dns.resolver.query(domain,'MX')	#查询MX记录
   ns = dns.resolver.query(domain,'NS')	#查询NS记录
   soa = dns.resolver.query(domain,'SOA') #查询SOA记录
   #cname = dns.resolver.query(domain,'CNAME') #查询CNAME记录
   #ptr = dns.resolver.query(domain,'PTR') #查询PTR记录
   for i in A.response.answer:	#通过response.answer 方法获取查询回应信息
	print i
	for  j in i.items:	#遍历回应信息
		print j.address
   print "-------------------"
   for i in MX:
	print 'MX preference =',i.preference, 'mail exchanger =',i.exchange
   print "-------------------"
   for i in ns.response.answer:
	for j in i.items:
		print j.to_text()
   print "-------------------"
   for i in soa.response.answer:
	for j in i.items:
		print j.to_text()
   print "-------------------"
#监控多IP域名的IP活动情况,原理:先利用dns.resolve解析出IP列表，然后利用httplib进行IP的活动判断
import httplib
iplist = []
domain = raw_input("监控的域名:")	#输入需要监控的域名,也可以在脚本中写死
def get_iplist(domain=""):
    try:
    	A = dns.resolver.query(domain,'A')
    except Exception,e:
	print "dns resolver error:"+str(e)
	return
    for i in A.response.answer:
	for j in i.items:
		iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip+":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)	#定义http连接超时时间
    conn = httplib.HTTPConnection(checkurl)	#创建http连接对象

    try:
	conn.request("GET","/",headers = {"Host":domain})	#发起url请求，添加host主机头
	r = conn.getresponse()
	getcontent = r.read(9)	#获取URL页面前15个字符，用于校验
	print getcontent
    finally:
	if getcontent =="<!DOCTYPE":	#监控URL也的内容一般是定义好的
		print ip +"[OK]"
	else:
		print ip+"[ERROR]"

def dns_monitor():
    if get_iplist(domain) and len(iplist) >0:
	for ip in iplist:
		checkip(ip)
    else:
	print "dns resolver error."
	

#----------------------07------------------------------------
