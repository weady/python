#!/usr/bin/python
#coding=utf-8
import logging
import paramiko
import sys,os,time
import re
import logging
import datetime
import threading
import Queue

reload(sys)
sys.setdefaultencoding('utf8')
'''
Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
Queue模块中的常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
datetime.now().strftime('%Y-%m-%d %H:%M:%S') 日期格式
'''

exitFlag = 0
queueLock = threading.Lock()
workQueue = Queue.Queue()


#定义下载文件类
class myThread(threading.Thread):
    def __init__(self, q, user, passwd):
        threading.Thread.__init__(self)
        self.user = user
        self.passwd = passwd
        self.q = q
    def run(self):
        work(self.q, self.user, self.passwd)

#封装的日志类

class Logger:
    def __init__(self,path,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        #设置文件日志
        fh = logging.FileHandler(path)
      	fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)

def work(q,user,passwd):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            host = q.get()
            process_data(host,user,passwd)
            queueLock.release()
        else:
	    print 'test'
            queueLock.release()
	    break
        time.sleep(1)

#处理函数
loginfo = Logger('/app/scripts/rsync_log_file.log', logging.INFO)
def process_data(host,user,passwd):

    HOST_NAME = host
    USER_NAME = user
    PASSWD = passwd

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    tmp_file_list = []
    try:
        ssh.connect(hostname = HOST_NAME, username = USER_NAME, password = PASSWD, timeout=5)
        stdin,stdout,stderr=ssh.exec_command(''' find /app/applogs* -type f -name "*.%s.log" ''' % yesterday ,timeout = 10)    
        for name in stdout.readlines():
            if name:
                tmp_file_list.append(name.strip('\n'))

    except Exception,e:
        loginfo.error(str(e))
	loginfo.error("[ %s ] 获取日志文件失败" % HOST_NAME)
	return 

    finally:
        ssh.close()


    #下载文件到本地

    ssh_download=paramiko.Transport((HOST_NAME,22))
    try:
        ssh_download.connect(username = USER_NAME,password = PASSWD)
        sftp=paramiko.SFTPClient.from_transport(ssh_download)
        for FILE in tmp_file_list:  
            file_name = HOST_NAME + '_' + os.path.split(FILE)[1]
            src_path = os.path.split(FILE)[0]
            tmp_dest_path = '/'.join(src_path.split('/')[3:])
	    year = datetime.datetime.now().strftime('%Y')
	    month = datetime.datetime.now().strftime('%m')
	    day = str(yesterday).split('-')[2]
            dest_path = os.path.join('/data_log/app/applogs',year,month,day,tmp_dest_path)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            dest_file = os.path.join(dest_path,file_name)
            loginfo.info("[ %s ] 下载%s日志文件到本地目录%s" % (HOST_NAME,FILE,dest_path))
            sftp.get(FILE,dest_file)

    except Exception as e:
	loginfo.error("[ %s ] 下载日志文件失败" % (HOST_NAME))
        loginfo.error(str(e))
	return 

    finally:
        ssh_download.close()

#获取主机列表
def get_client_ip():
        mysql_info = {
                "cmdb_user": "cmdb",
                "cmdb_passwd": "123456",
                "cmdb_host": "192.168.1.1",
                "cmdb_db_name": "cmdb"
        }

        sql=""" select * from xxx"""
        db = MySQLdb.connect(mysql_info["cmdb_host"],mysql_info["cmdb_user"],mysql_info["cmdb_passwd"],mysql_info["cmdb_db_name"],charset='utf8')
        cursor = db.cursor()
        try:
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
                raise e
        finally:
                cursor.close()
                db.close()

#获取主机列表从文件中
def get_hosts_list():
	host_list = []
	with open("ip.txt") as f:
		for line in f:
			if line:
				host_list.append(line.strip('\n'))
	return host_list

#日志会滚功能
def roll_back_log():
	yesterday = datetime.date.today() - datetime.timedelta(days=3)

	with open("/app/scripts/rsync_log_file.log","r") as f:
    		lines = f.readlines()

	with open("/app/scripts/rsync_log_file.log","w") as f_w:
    		for line in lines:
			if str(yesterday) in line and line:
         	   		continue

        		f_w.write(line)


#主函数
def main():
    IP_List = get_hosts_list()

    threads = []

    # 创建新线程
    for i in range(1,21):
        th = myThread(workQueue,'xxxx','xxxxxx')
        threads.append(th)

    #启动线程
    for t1 in threads:
        t1.start()

    # 填充队列
    queueLock.acquire()
    for IP in IP_List:
        workQueue.put(IP)
    queueLock.release()

    # 等待队列清空
    #while not workQueue.empty():
    #    pass

    # 通知线程是时候退出
    exitFlag = 1

    # 等待所有线程完成
    for t2 in threads:
        t2.join()


if __name__ == "__main__":
	main()
	
	roll_back_log()
