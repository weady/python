#!/usr/bin/python
#coding:utf-8
#这个脚本是socket通信中的服务端代码
#
#	by wangdd 2016/2/20

import socket,commands
import SocketServer
import time
#单进程的socket通信,利用的模块是socket commands模块
def single_socket():
    host = '192.168.36.130'
    port = 51000

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(1)

    while 1:
    	conn,addr = s.accept()
    	print 'Conneted by',addr
	while 1:
		data = conn.recv(1024)
		if not data:break
		cmd_status,result = commands.getstatusoutput(data)
		if len(result) !=0:
			conn.sendall(result)
		else:
			conn.sendall('Done')
    conn.close()

#多线程的socket通信利用的socketserver模块,该模块默认支持多线程
class MyTCPHandler(SocketServer.BaseRequestHandler):
    number = 0
    def handle(self):
	while 1:
		self.data =self.request.recv(1024).strip()
		self.number += 1
		print self.client_address[0],self.number
		if not self.data:
			print "Client %s is break." % self.client_address[0]
			break
		user_input = self.data.split()
		if user_input[0] == 'get':
			print "\033[1;32m Starting transfer file to %s\033[1;m " % self.client_address[0]
			with open(user_input[1],'rb') as f:
				self.request.sendall(f.read())
			time.sleep(0.3)
			self.request.send("Filetransferover")
			continue
		cmd_status,result = commands.getstatusoutput(self.data)
                if len(result.strip()) !=0:
                        self.request.sendall(result)
                else:
                        self.request.sendall('Done')
if __name__ == "__main__":
    host,port = "192.168.36.130",52000
    server =SocketServer.ThreadingTCPServer((host,port),MyTCPHandler)
    server.serve_forever()
