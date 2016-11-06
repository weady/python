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
'''
subprocess.call()
	父进程等待子进程完成
	返回退出信息(returncode，相当于exit code)
subprocess.check_call()
	父进程等待子进程完成
	返回0
	检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError
subprocess.check_output()
	父进程等待子进程完成
	返回子进程向标准输出的输出结果
	检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError
Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待
Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)
	stdin stdout stderr
	subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本
	child = subprocess.Popen(["cat"], stdin=subprocess.PIPE)
	child.communicate("vamei")
	cat会等待输入，直到我们用communicate()输入"vamei"
'''
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
#domain = raw_input("监控的域名:")	#输入需要监控的域名,也可以在脚本中写死
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
#difflib 模块实现两个字符串的差异比较
import difflib
import sys
def com_string():
    text1 = '''This is a test string v0.1
	add
	'''
    text2 = '''This is a test string v0.2'''
    text1_line = text1.splitlines()	#以行进行分割,以便进行对比
    text2_line = text2.splitlines()
    d = difflib.Differ()	#创建Differ()对象
    diff_html = difflib.HtmlDiff()	# 使用htmlDiff生成html类型的类
    diff = d.compare(text1_line,text2_line)
    #print '\n'.join(list(diff))
    #print "----------------------------------"
    print diff_html.make_file(text1_line,text2_line)	#使用make_file()方法生成美观的HTML文档

def readfile(filename):
    try:
	file_read = open(filename,'rb')
	text = file_read.read().splitlines()
	file_read.close
	return text
    except IOError as error:
	print "read file error"+str(error)
	sys.exit()

def com_file():
    try:
	file1 = sys.argv[1]
	file2 = sys.argv[2]
    except Exception,e:
	print "Error:"+str(e)
	print "Usage: python.model.py file1 file2"
    if file1 =="" or file2 =="":
	print "usage: $s file1 file2" % sys.argv[0]
	sys.exit()
    text1_line = readfile(file1)
    text2_line = readfile(file2)
    d = difflib.HtmlDiff()
    print d.make_file(text1_line,text2_line)

#----------------------07------------------------------------
#filecmp 模块实现文件、目录、遍历子目录的差异对比功能

import filecmp

def com_dir():
    a = sys.argv[1]	#外部传入的第一个参数，作为左目录        
    b = sys.argv[2]	#外部传入的第二个参数，作为右目录
    dirobj=filecmp.dircmp(a,b,['test.py']) 	#目录比较,忽略test.py文件

    #输出对比结果数据报表
    dirobj.report() #比较当前指定目录中的内容
    dirobj.report_partial_closure()	#比较当前指定目录及第一子目录中的内容
    dirobj.report_full_closure()	#递归比较所有指定目录的内容

    print "left_list:" + str(dirobj.left_list)	#只列出当前目录下的，没有对子目录进行分析
    print "right_list:" + str(dirobj.right_list)
    print "common:" + str(dirobj.common)
    print "left_only:" + str(dirobj.left_only)
    print "right_only:" + str(dirobj.right_only)
    print "common_dirs:" + str(dirobj.common_dirs)	#两边目录都存在的子目录
    print "common_files:" + str(dirobj.common_files)	#两边目录都存在的子文件
    print "common_funny:" + str(dirobj.common_funny)	#两边目录都存在的子目录
    print "same_files:" + str(dirobj.same_files)	#匹配相同的文件
    print "diff_files:" + str(dirobj.diff_files)	#不匹配的文件
    print "funny_files:" + str(dirobj.funny_files)	#两边目录中都存在,但无法比较的文件

#校验源与备份目录差异，使用filecmp模块的left_only,diff_files方法递归获取源目录的更新项,再通过shutil.copyfile
#os.makedirs 方法对更新项进行复制，最终保持一致状态
#使用到的模块有os,sys filecmp re shutil 
import re
import shutil
holderlist = []

def compare(dir1,dir2):	#递归获取更新项函数
    dircomp = filecmp.dircmp(dir1,dir2)
    only_in_src = dircomp.left_only	#源目录新文件或目录
    diff_in_src = dircomp.diff_files	#不匹配文件,源目录文件已发生变化
    dirpath = os.path.abspath(dir1)	#定义源目录绝对路径
    #将更新的文件名或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_src]    
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_src]    
    
    if len(dircomp.common_dirs) >0:	#判断是否存在相同的字目录，以便递归
	for item in dircomp.common_dirs:	#递归子目录
		compare(os.path.abspath(os.path.join(dir1,item)),os.path.abspath(os.path.join(dir2,item)))
    return holderlist	#返回的是源目录中的新文件和变化的文件列表

def compare_main():
    if len(sys.argv) >2:
	dir1 = sys.argv[1]
	dir2 = sys.argv[2]
    else:
	print "Usage:",sys.argv[0],"datadir backupdir"
	sys.exit()

    source_files=compare(dir1,dir2)	#对比源目录和备份目录
    dir1 = os.path.abspath(dir1)

    if not dir2.endswith('/'):dir2 = dir2+'/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    for item in source_files:	#遍历返回的差异文件或目录清单
	destination_dir = re.sub(dir1,dir2,item)	#将源目录差异路径清单对应替换成备份目录

	destination_files.append(destination_dir)
	if os.path.isdir(item):
		if not os.path.exists(destination_dir):
			os.makedirs(destination_dir)
			createdir_bool = True

	if createdir_bool:
		destination_files = []
		source_files =[]
		source_files = compare(dir1,dir2)
		for item in source_files:
			destination_dir = re.sub(dir1,dir2,item)
			destination_files.append(destination_dir)

	print "update item:"
	print source_files	#输出更新列表清单
	copy_pair = zip(source_files,destination_files)	#将源目录与备份目录文件清单拆分成元组
	for item in copy_pair:
		if os.path.isfile(item[0]):	#判断是否为文件,是则进行复制操作
			shutil.copy2(item[0],item[1])

#----------------------08------------------------------------
#pycurl 支持ftp,http,https,telnet 类似linux下的curl命令，可以实现探测web服务质量情况
#----------------------09------------------------------------
#csv 模块
import csv
def csv_mode():
	rows = [{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
	{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
	{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
	{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
	{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}]

	fieldnames = ['Column1', 'Column2', 'Column3', 'Column4']
	dict_writer = csv.DictWriter(open(r'my.csv', 'wb'), fieldnames=fieldnames)
	dict_writer.writeheader() #写入首行
	dict_writer.writerows(rows)

#----------------------10------------------------------------
#fileinput 模块
'''
fileinput.input()返回能够用于for循环遍历的对象
fileinput.filename()返回当前文件的名称
fileinput.lineno()返回当前已经读取的行的数量
fileinput.filelineno()返回当前读取的行的行号
fileinput.isfirstline()判断最后一个是否从stdin中读
fileinput.close()关闭队列
'''
#----------------------11------------------------------------
#argparse模块的作用是用于解析命令行参数
'''
1：import argparse
2：parser = argparse.ArgumentParser() 
	方法ArgumentParser(prog=None, usage=None,description=None, epilog=None, parents=[],formatter_class=argparse.HelpFormatter,
	prefix_chars='-',fromfile_prefix_chars=None, argument_default=None,conflict_handler='error', add_help=True)
	一般只需要传递description参数
3：parser.add_argument()
	方法add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
	nargs：命令行参数的个数，一般使用通配符表示，其中，'?'表示只用一个，'*'表示0到多个，'+'表示至少一个
	dest: 这个参数相当于把位置或者选项关联到一个特定的名字
	metavar: 这个参数用于help 信息输出中
4：parser.parse_args()
'''
import argparse

def parse_arg():
	description = 'This is a test'
	parser = argparse.ArgumentParser(description = description)
	parser.add_argument('address',nargs = '*',help='arg list')
	parser.add_argument('-p','--port',type=int,help='arg type')
	args = parser.parse_args();
	return args

args = parse_arg()
for address in args.address:
	print 'IP address is : %s .' % address
print 'Type is : %s .' % args.port

#----------------------12------------------------------------
#getpass 模块可以对输入的密码不在终端显示明文
'''
当输入为纯数字时
    input返回的是数值类型，如int,float
    raw_inpout返回的是字符串类型，string类型
输入字符串为表达式
    input会计算在字符串中的数字表达式，而raw_input不会
'''
	user = raw_input('Please input user name:')
	passwd = getpass.getpass('Please input your password:')

#----------------------13------------------------------------
#configparser 模块读取配置文件
'''
1.初始化:
	使用ConfigParser 首选需要初始化实例，并读取配置文件
	cf = ConfigParser.ConfigParser()
	cf.read("配置文件名")
2.ConfigParser 常用方法
	获取所有sections。也就是将配置文件中所有“[ ]”读取到列表中
	s = cf.sections()
	获取指定section 的options。即将配置文件某个section 内key 读取到列表中
	o = cf.options("db")
	获取指定section 的配置信息
	v = cf.items("db")
	按照类型读取指定section 的option 信息,同样的还有getfloat、getboolean,getint
	db_host = cf.get("db", "db_host")
	设置某个option 的值
	cf.set("db", "db_pass", "zhaowei")
	cf.write(open("test.conf", "w"))
	添加一个section
	cf.add_section('liuqing')
	删除一个seciion 或者option
	cf.remove_option('liuqing','int')
	cf.remove_section('liuqing')
	cf.write(open("test.conf", "w"))



'''

#----------------------14------------------------------------
#webbrowser 模块启动一个浏览器
#import webbroweser
#webbrowser.open('http://www.python.org') webbrowser.open_new_tab('http://www.python.org')
#c = webbrowser.get('firefox')  c.open('http://www.python.org')
