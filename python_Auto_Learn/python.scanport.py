#/usr/bin/env python
#coding=utf-8
#
#
#	by wangdd 2016/03/17

#python-nmap模块实现端口扫描,yum install nmap
#python-nmap模块的两个常用类,PortScanner()----实现端口扫描功能;
#PortScannerHostDict()--->实现存储和访问主机的扫描结果

import nmap
import sys

def port_scan():
    scan_row = []
    input_data = raw_input('Please input hosts and ports:')
    scan_row = input_data.split(" ")
    if len(scan_row) !=2:
	print "输入错误,应输入\"192.168.1.0/24 22,3306\""
	sys.exit(1)
    hosts = scan_row[0]
    ports = scan_row[1]

    try:
	nm = nmap.PortScanner() #创建端口扫描对象
    except nmap.PortScannerError:
	print "Nmap not found"
	sys.exit(0)
    except:
	print "Unexpected error"
	sys.exit(0)

    try:
	#调用扫描方法,参数指定扫描主机hosts,nmap扫描命令行参数arguments
	nm.scan(hosts=hosts,arguments=' -v -sS -p'+ ports)
    except Exception,e:
	print "Scan error:" + str(e)

    for host in nm.all_hosts():
	print ('-------------------')
	print ('Host : %s (%s)' % (host,nm[host].hostname()))
	print ('State : %s' % nm[host].state())

    	for proto in nm[host].all_protocols():
		print '--------------------'
		print 'Protocol : %s' % proto

		lport = nm[host][proto].keys()
		lport.sort()

		for port in lport:
			print 'Port : %s\t state : %s' % (port,nm[host][proto][port]['state'])

port_scan()
