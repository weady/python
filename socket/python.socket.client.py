#!/usr/bin/python
#coding:utf-8
#
#这个脚本是socket通信的客户端代码
#
#	by wangdd 2016/2/20

import socket,time

host = '192.168.36.130'
port = 52000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    cmd = raw_input("输入要执行的命令:").strip()
    if len(cmd)==0:continue
    s.sendall(cmd)
    if cmd.split()[0] == 'get':
	print "Start downlading file....."
	with open(cmd.split()[1],'wb') as f:
		while 1:
			data = s.recv(1024)
			if data == "Filetransferover":break
			f.write(data)
	continue
    else:
    	print s.recv(1024)
s.close()

#udp协议的客户端
def UDPCLIENT():
        HOST = '192.168.36.108'
        PORT = 21567
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        udpclient = socket(AF_INET,SOCK_DGRAM)

        while True:
                data = raw_input('>')
                if not data:
        	       break
                udpclient.sendto(data,ADDR)
                data,ADDR = udpclient.recvfrom(BUFSIZE)
                if not data:
                        break
                print data
        udpclient.close()
        
 
