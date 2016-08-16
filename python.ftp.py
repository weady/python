#coding: utf-8
from ftplib import FTP
import time
import tarfile
import socket
import os


#ftp基本操作
	'''
	ftp登陆连接
	from ftplib import FTP            #加载ftp模块
	ftp=FTP()                         #设置变量
	ftp.set_debuglevel(2)             #打开调试级别2，显示详细信息
	ftp.connect("IP","port")          #连接的ftp sever和端口
	ftp.login("user","password")      #连接的用户名，密码
	print ftp.getwelcome()            #打印出欢迎信息
	ftp.cmd("xxx/xxx")                #进入远程目录
	bufsize=1024                      #设置的缓冲区大小
	filename="filename.txt"           #需要下载的文件
	file_handle=open(filename,"wb").write #以写模式在本地打开文件
	ftp.retrbinaly("RETR filename.txt",file_handle,bufsize) #接收服务器上文件并写入本地文件
	ftp.set_debuglevel(0)             #关闭调试模式
	ftp.quit()                        #退出ftp
	 
	ftp相关命令操作
	ftp.cwd(pathname)                 #设置FTP当前操作的路径
	ftp.dir()                         #显示目录下所有目录信息
	ftp.nlst()                        #获取目录下的文件
	ftp.mkd(pathname)                 #新建远程目录
	ftp.pwd()                         #返回当前所在位置
	ftp.rmd(dirname)                  #删除远程目录
	ftp.delete(filename)              #删除远程文件
	ftp.rename(fromname, toname)#将fromname修改名称为toname。
	ftp.storbinaly("STOR filename.txt",file_handel,bufsize)  #上传目标文件
	ftp.retrbinary("RETR filename.txt",file_handel,bufsize)  #下载FTP文件
	'''

#ftp基本函数模板
def ftptest():      
	ftp = FTP()  
	timeout = 30  
	port = 21  
	ftp.connect('192.168.1.188',port,timeout) # 连接FTP服务器  
	ftp.login('UserName','888888') # 登录  
	print ftp.getwelcome()  # 获得欢迎信息   
	ftp.cwd('file/test')    # 设置FTP路径  
	list = ftp.nlst()       # 获得目录列表  
	for name in list:  
	    print(name)             # 打印文件名字  
	path = 'd:/data/' + name    # 文件保存路径  
	f = open(path,'wb')         # 打开要保存文件  
	filename = 'RETR ' + name   # 保存FTP文件  
	ftp.retrbinary(filename,f.write) # 保存FTP上的文件  
	ftp.delete(name)            # 删除FTP文件  
	ftp.storbinary('STOR '+filename, open(path, 'rb')) # 上传FTP文件  
	ftp.quit()                  # 退出FTP服务器  

#ftp文件的上传和下载

def ftpconnect(host, username, password):
    ftp = FTP()
    #ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, 21)          #连接
    ftp.login(username, password)  #登录，如果匿名登录则用空串代替即可
    return ftp
    
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024                #设置缓冲块大小
    fp = open(localpath,'wb')     #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)         #关闭调试
    fp.close()                    #关闭文件

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize) #上传文件
    ftp.set_debuglevel(0)
    fp.close()                                    

if __name__ == "__main__":
    ftp = ftpconnect("******", "***", "***")
    downloadfile(ftp, "***", "***")
    uploadfile(ftp, "***", "***")

    ftp.quit()

#ftp 异常处理 


def ftpconnect(ftp_info):
    try:
        ftp = ftplib.FTP(ftp_info[0])
    except (socket.error, socket.gaierror):
        print "ERROR: cannot reach %s" % ftp_info[0]
        return None

    username = ftp_info[1]
    passwd = ftp_info[2]
    try:
        ftp.login(username, passwd)
    except ftplib.error_perm:
        print "ERROR: cannot login anonymously"
        ftp.quit()
        return None
    return ftp

if __name__ == "__main__":
    info_list = ["10.19.3.199", "fastupdate_amap", "@utonavi&A.map"]
    ftp = ftpconnect(info_list)
    if not ftp:
        exit(1)
    bufsize = 1024
    fname = "20150416113942674.tar.gz"
    fp = open(os.path.join(".", fname), 'wb')
    remotefile = os.path.join("/ADF++", fname)
    ftp.retrbinary("RETR " + remotefile, fp.write, bufsize)

    #是否有目录，没有就创建；有的话看是否有权限创建
    a = ftp.dir()
    try:
        ftp.cwd("jimi")
    except ftplib.error_perm:
        try:
            ftp.mkd("jimi")
        except ftplib.error_perm:
            print "WARNING: U have no authority to make dir"
    finally:
        ftp.quit()

#ftp 上传和下载文件/目录 目录的内容需为文件
from ctypes import *
import os
import sys
import ftplib

class myFtp:
    ftp = ftplib.FTP()
    bIsDir = False
    path = ""
    def __init__(self, host, port='21'):
        #self.ftp.set_debuglevel(2) #打开调试级别2，显示详细信息 
        #self.ftp.set_pasv(0)      #0主动模式 1 #被动模式
        self.ftp.connect( host, port )
            
    def Login(self, user, passwd):
        self.ftp.login( user, passwd )
        print self.ftp.welcome

    def DownLoadFile(self, LocalFile, RemoteFile):
        file_handler = open( LocalFile, 'wb' )
        self.ftp.retrbinary( "RETR %s" %( RemoteFile ), file_handler.write ) 
        file_handler.close()
        return True
    
    def UpLoadFile(self, LocalFile, RemoteFile):
        if os.path.isfile( LocalFile ) == False:
            return False
        file_handler = open(LocalFile, "rb")
        self.ftp.storbinary('STOR %s'%RemoteFile, file_handler, 4096)
        file_handler.close()
        return True

    def UpLoadFileTree(self, LocalDir, RemoteDir):
        if os.path.isdir(LocalDir) == False:
            return False
        print "LocalDir:", LocalDir
        LocalNames = os.listdir(LocalDir)
        print "list:", LocalNames
        print RemoteDir
        self.ftp.cwd( RemoteDir )
        for Local in LocalNames:
            src = os.path.join( LocalDir, Local)
            if os.path.isdir( src ): self.UpLoadFileTree( src, Local )
            else:
                self.UpLoadFile( src, Local )
                
        self.ftp.cwd( ".." )
        return
    
    def DownLoadFileTree(self, LocalDir, RemoteDir):
        print "remoteDir:", RemoteDir
        if os.path.isdir( LocalDir ) == False:
            os.makedirs( LocalDir )
        self.ftp.cwd( RemoteDir )
        RemoteNames = self.ftp.nlst()  
        print "RemoteNames", RemoteNames
        print self.ftp.nlst("/del1")
        for file in RemoteNames:
            Local = os.path.join( LocalDir, file )
            if self.isDir( file ):
                self.DownLoadFileTree( Local, file )                
            else:
                self.DownLoadFile( Local, file )
        self.ftp.cwd( ".." )
        return
    
    def show(self, list):
        result = list.lower().split( " " )
        if self.path in result and "<dir>" in result:
            self.bIsDir = True
     
    def isDir(self, path):
        self.bIsDir = False
        self.path = path
        #this ues callback function ,that will change bIsDir value
        self.ftp.retrlines( 'LIST', self.show )
        return self.bIsDir
    
    def close(self):
        self.ftp.quit()

if __name__ == "__main__":
    ftp = myFtp('*****')
    ftp.Login('***','***')

    ftp.DownLoadFileTree('del', '/del1')#ok
    ftp.UpLoadFileTree('del', "/del1" )
    ftp.close()
    print "ok!"
