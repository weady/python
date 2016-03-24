#!/usr/bin/env python
#coding=utf-8
#
#
#	by wangdd 2016/03/22

#系统批量运维管理器paramiko 
#pip install paramiko;yum install python-devel pycrypto ecdsa

#paramiko 核心组件,SSHClient类，SFTPClient类
#SSHClient 类是ssh服务会话的高级表示，封装了transport channel SFTPClient的校验，建立的方法，通常用于执行远程命令
#SFTPClient 实现远程文件操作，上传，下载，权限，状态等

import paramiko
import sys,os,time

#利用账号密码的方式使用ssh
def auto_ssh():
	hostname = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]
	paramiko.util.log_to_file('syslogin.log')	#发送paramiko日志到syslogin.log文件

	ssh = paramiko.SSHClient()	#创建一个ssh客户端client对象
	ssh.load_system_host_keys()	#获取客户端host_keys,默认~/.ssh/known_hosts,非默认路径需指定

	ssh.connect(hostname=hostname,username=username,password=password)	#创建ssh连接

	stdin,stdout,stderr = ssh.exec_command('free -m') #调用远程执行命令方法，exec_command()
	print stdout.read()
	ssh.close()

#利用密钥的方式登录远程主机,需要首先做好服务器间的无密码访问
def no_passwd_ssh():
	hostname = sys.argv[1]
	username = sys.argv[2]
	paramiko.util.log_to_file('syslogin.log')	#发送paramiko日志到syslogin.log文件
	
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	privatekey = os.path.expanduser('/root/.ssh/id_rsa')	#定义私钥存放路径
	key = paramiko.RSAKey.from_private_key_file(privatekey)	#创建私钥对象key

	ssh.connect(hostname=hostname,username=username,pkey=key)
	stdin,stdout,stderr = ssh.exec_command('free -m') #调用远程执行命令方法，exec_command()
	print stdout.read()
	ssh.close()

#实现堡垒机模式下远程命令执行
def bl_exec_command():
	blip = "192.168.1.200"
	bluser = "wangdong"
	blpasswd = "wangdong"

	hostname = "192.168.1.200"
	username = "wangdong"
	password = "wangdong"

	port = 22
	passinfo = '\'s password: '	#输入服务器密码的前标识串
	paramiko.util.log_to_file('syslogin.log')
	
	#登录堡垒机
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=blip,username=bluser,password=blpasswd)
	
	channel = ssh.invoke_shell()	#创建会话,开启命令调用
	channel.settimeout(10)	#会话命令执行超时时间，单位为妙

	buff = ''
	resp = ''
	channel.send('ssh '+username+'@'+hostname+'\n') #执行ssh登录业务主机
	while not buff.endswith(passinfo):
		try:
			resp = channel.recv(9999)
		except Exception,e:
			print 'Error info:%s connection time.' % (str(e))
			channel.close()
			ssh.close()
			sys.exit()
		buff += resp
		if not buff.find('yes/no') ==-1:
			channel.send('yes\n')
			buff=''

	
	channel.send(password+'\n')

	buff = ''
	while not buff.endswith('$ '):
		resp = channel.recv(9999)
		if not resp.find(passinfo)==-1:
			print 'Error info:Authentication failed.'
			channel.close()
			ssh.close()
			sys.exit()
		buff +=resp

	channel.send('ifconfig\n')	#认证通过后发送ifconfig命令来查看结果
	buff=''
	try:
		while buff.find('$ ')==-1:
			resp = channel.recv(9999)
			buff+= resp
	except Exception,e:
		print 'Error info:' + str(e)

	print buff	#打印输出串
	channel.close()
	ssh.close()

	
bl_exec_command()
