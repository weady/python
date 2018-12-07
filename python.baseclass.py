#-*- coding:utf8 -*-
#   by wangdd 2016/06/23

import re #正则表达式模块
import os, sys, time
import Queue, threading, subprocess
import logging
import json
from multiprocessing import Pool
import nmap
import MySQLdb #数据库连接模块
import xlrd,xlwt
import socket

reload(sys)
sys.setdefaultencoding('utf8')

#日志处理类s
class Logger(object):
    #日志模块操作的经典例子,CMD窗口和日志文件两种方式记录日志
    """
    logger = logging.getLogger("simple_example")
    logger.setLevel(logging.DEBUG) 
    # 建立一个filehandler来把日志记录在文件里，级别为debug以上 
    fh = logging.FileHandler("spam.log") 
    fh.setLevel(logging.DEBUG) 
    # 建立一个streamhandler来把日志打在CMD窗口上 级别为error以上 
    ch = logging.StreamHandler() 
    ch.setLevel(logging.ERROR) 
    # 设置日志格式 
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") 
    ch.setFormatter(formatter) 
    fh.setFormatter(formatter) 
    #将相应的handler添加在logger对象中 
    logger.addHandler(ch) 
    logger.addHandler(fh) 
    # 开始打日志 logger.debug("debug message") 

    """

    def __init__(self,path,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[ %(asctime)s ] [ %(levelname)s ] - %(message)s', '%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        #设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        
        # self.logger.addHandler(sh) #终端显示日志
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    
    def info(self,message):
        self.logger.info(message)
        logging.shutdown()

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)

    #使用方式
    #loginfo = Logger('wangdong.log',logging.ERROR, logging.DEBUG) 实例化
    #loginfo.debug('debug message')

#数据库处理类
class db_sql(object):

        def __init__(self, user='root', passwd='123456', host='127.0.0.1', db_name='matrix'):

            self.user = user
            self.passwd = passwd
            self.host = host
            self.db_name = db_name

        def db_deal_data(self,sql,param=0):
            '''
            定义了数据库查询和插入的方法
            @sql 是传入的sql语句
            @param 是在进行批量插入数据时，传入的数据列表或元组

            '''
            self.sql = sql
            self.param = param

            db = MySQLdb.connect(self.host,self.user,self.passwd,self.db_name,charset='utf8')
            #cursor()方法获取操作游标
            cursor = db.cursor()
            if param:
                try:
                    cursor.executemany(sql,param) #使用executemany 批量插入数据,param为列表或元组类型
                    db.commit()
                    return "数据插入成功"
                except Exception,e:
                    db.rollback()
                    return str(e)
                finally:
                    db.close()
            else:
                cursor.execute(sql) #执行单条sql语句，得到查询结果并返回
                result = cursor.fetchall()
                cursor.close()
                db.close()
                return result

        def db_update_data(self,sql):
            """
            @sql 更新语句
            """
            self.sql = sql

            db = MySQLdb.connect(self.host,self.user,self.passwd,self.db_name,charset='utf8')
            #cursor()方法获取操作游标
            cursor = db.cursor()
            try:
                cursor.execute(self.sql)
                db.commit()
                return "数据插入成功"
            except Exception,e:
                db.rollback()
                return str(e)
            finally:
                db.close()

        def safe(self,s):
            self.s = s
            return MySQLdb.escape_string(s)

        def get_i_sql(self, table, dict):
            '''
            生成insert的sql语句
            @table，插入记录的表名
            @dict,插入的数据，字典
            '''
            self.table = table
            self.dict = dict
            sql = 'insert into %s set ' % table
            sql += self.dict_2_str(dict)
            return sql

        def get_insert_sql(self,table,column_list):
            '''
            生成insert的sql语句
            @table，插入记录的表名
            @column_list,插入的列信息
            '''
            self.table = table
            self.column_list = column_list
            if table and column_list:
                sql = 'insert into %s%s' % (table,self.deal_column_list(column_list))
            return sql

        def get_replace_sql(self,table,column_list):
            '''
            生成insert的sql语句
            @table，插入记录的表名
            @column_list,插入的列信息
            '''
            self.table = table
            self.column_list = column_list
            if table and column_list:
                sql = 'replace into %s%s' % (table,self.deal_column_list(column_list))
            return sql

        def get_s_sql(self, table, keys, conditions=0, isdistinct=0, selecttype='accurate'):
            '''
            生成select的sql语句
            @table，查询记录的表名
            @key，需要查询的字段
            @conditions,查询的数据，字典
            @isdistinct,查询的数据是否不重复
            @selecttype,是模糊查询还是精确查询
            '''
            self.table = table
            self.keys = keys
            self.conditions = conditions
            self.isdistinct = isdistinct
            self.selecttype = selecttype
            if isdistinct:
                sql = 'select distinct %s ' % ",".join(keys)
            else:
                sql = 'select  %s ' % ",".join(keys)
            sql += ' from %s ' % table
            if selecttype == 'accurate' and conditions:
                sql += ' where %s ' % self.dict_2_str_and(conditions)
            elif selecttype == 'vague' and conditions:
                sql += ' where %s ' % self.dict_2_str_like(conditions)
            return sql

        def get_u_sql(self,table, value, conditions):
            '''
            生成update的sql语句
            @table，查询记录的表名
            @value，dict,需要更新的字段
            @conditions,插入的数据，字典
            '''
            self.table = table
            self.value = value
            self.conditions = conditions

            sql = 'update %s set ' % table
            sql += self.dict_2_str(value)
            if conditions:
                sql += ' where %s ' % self.dict_2_str_and(conditions)
            return sql

        def get_d_sql(self, table, conditions):
            '''
            生成detele的sql语句
            @table，查询记录的表名

            @conditions,插入的数据，字典
            '''
            self.table = table
            self.conditions = conditions
            sql = 'delete from  %s  ' % table
            if conditions:
                sql += ' where %s ' % self.dict_2_str_and(conditions)
            return sql

        def dict_2_str(self, dictin):
            '''
            将字典变成，key='value',key='value' 的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ','.join(tmplist)

        def dict_2_str_and(self, dictin):
            '''
            将字典变成，key='value' and key='value'的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ' and '.join(tmplist)

        def dict_2_str_like(self, dictin):
            '''
            将字典变成，key like 'value' and key like 'value'的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s like '%%%s%%'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ' and '.join(tmplist)

        def deal_column_list(self, col_list):
            '''
            列表是要插入数据的列信息，转换成(a,b,c,) value(%s,%s,%s) 的形式
            '''
            self.col_list = col_list
            tmplist =[]
            if len(col_list) > 0:
                for i in range(0,len(col_list)):
                    t = "%s"
                    tmplist.append(t)
                return '(' + ','.join(col_list) + ')' + " " + str('value') + '(' + ','.join(tmplist) + ')'

#定义一个SSH远程操作的类
class sshconn(object):
    '''
    这个类主要用户与SSH远程主机并执行命令
    '''
    def __init__(self,hostlist,username,command):
        self.hostlist = hostlist
        self.username = username
        self.command = command
        self.q = Queue.Queue()

    def ssh(self,hostname,username,command):
        #paramiko.util.log_to_file('syslogin.log')   #发送paramiko日志到syslogin.log文件
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.load_system_host_keys()
            privatekey = os.path.expanduser('/root/.ssh/id_rsa')    #定义私钥存放路径
            key = paramiko.RSAKey.from_private_key_file(privatekey) #创建私钥对象key
            ssh.connect(hostname=hostname,username=username,pkey=key)
            if command == 'top':
                command = 'top -b n 1'
            stdin,stdout,stderr = ssh.exec_command(command) #调用远程执行命令方法，exec_command()
            out = stdout.read()
            rest = "----------------------------------------------------%s------------------------------------------------\n%s" % (hostname,out)
            ssh.close()
            self.q.put(rest)
        except Exception,e:
            error_info = "----------------------------------------------------%s------------------------------------------------\n%s\n" % (hostname,str(e))
            self.q.put(error_info)

    def sshentrance(self):
        work_threads = []
        result = list()
        for ip in self.hostlist:
            th = threading.Thread(target=self.ssh, args=(ip,self.username,self.command))
            work_threads.append(th)
        for th in work_threads:
            th.start()

        for th in work_threads:
            threading.Thread.join(th)

        while not self.q.empty():
            result.append(self.q.get())
        return result

#定义一个操作excel文件的类型，实现从excel文件直接导入数据入库
class deal_excel(object):
    """
    xlrd模块读取excel文件的基础知识

    打开一个excel文件
    data = xlrd.open_workbook('auto_operation.xlsx')

    table = data.sheets()[0] #通过索引顺序获取一个工作表

    table = data.sheet_by_index(0) #通过索引顺序获取一个工作表

    table = data.sheet_by_name(u'sheet1') #通过名字获取

    table.row_values(i) #获取整行的值
    table.col_values(i) #获取整列的值

    nrows = table.nrows #获取行数
    ncols = table.ncols #获取列数

    循环行列表数据
    for i in range(nrows):
        #print table.row_values(i)

    使用行列索引

    cell_A1 = table.row(0)[0].value
    cell_A2 = table.col(1)[0].value
    """

    #根据名称获取excel表格中的数据 参数:file excel文件名 colnameindex 表头列名所在行的索引  sheet_name:sheet的名称

    def excel_data_byname(self, filename, sheet_name):
        sheets_list = []
        try:
            data = xlrd.open_workbook(filename)
            for i in xrange(len(data.sheets())):
                tmp_sheet_name = data.sheets()[i].name
                sheets_list.append(tmp_sheet_name)
        except Exception, e:
            print str(e)


        if sheet_name in sheets_list:
            table = data.sheet_by_name(sheet_name)
            nrows = table.nrows #行数
            self.colnameindex = 1
            colnames =  table.row_values(self.colnameindex) #某一行数据
            list_data =[]
            for rownum in range(2,nrows):
                row = table.row_values(rownum)
                if row:
                    list_data.append(row)
        else:
            colnames = None
            list_data = None

        return colnames, list_data

#利用pexpect
class nopassAuth(object):
    """
    利用pexpect模块实现无密的自动配置
    @password 目标主机的登录密码
    @desthost 目标主机列表
    """
    def __init__(self,password,desthost):
        self.password = password
        self.desthost = desthost
        self.result_list = []
        self.lock = threading.Lock()
        self.list_lock = threading.Lock()

    def test_auth(self,name):
        '''
        先判断主机是否授权过,如果授权过就不再进行授权
        '''
        T_child = pexpect.spawn('ssh %s "hostname"' % name)
        try:
            T = T_child.expect(['continue connecting (yes/no)?','password:'])
            if T == 0 or T == 1:
                return 'OK'
        except pexpect.EOF:
            T_child.close()

    def build_ssh_task(self,host):
        ssh_status = self.test_auth(host)
        result = '%s 已认证成功' % host

        if ssh_status == 'OK':
            if os.path.isfile('/root/.ssh/id_rsa.pub'):
                child=pexpect.spawn('ssh-copy-id -i /root/.ssh/id_rsa.pub "%s"' % (host),timeout=3)
                try:
                    i=child.expect(['[Pp]assword:','continue connecting (yes/no)?'])
                    if i == 0:
                        child.sendline(self.password)
                        index = child.expect(['Permission denied'])
                        if i == 0:
                            result = "%s 登录密码错误" % host
                            self.result_list.append(result)
                            sys.exit(1)
                    elif i == 1:
                        child.sendline('yes')
                        child.sendline(self.password)

                except pexpect.EOF,pexpect.TIMEOUT:
                    child.close()
                else:
                    result = "%s 无密配置成功" % host
                    child.close()
            else:
                result = "本机不存在'id_rsa.pub'文件"

        self.list_lock.acquire()
        self.result_list.append(result)
        self.list_lock.release()

    def ssh_work(self,index):
        while True:
            time.sleep(0.2)
            if len(self.desthost) >0:
                self.lock.acquire()
                self.ip = self.desthost.pop(0)
                self.lock.release()
                if self.ip:
                    self.build_ssh_task(self.ip)
            else:
                break

    def build_ssh_auth(self):
        '''
        配置无密访问的入口,根据主机数量生成相应的线程数进行配置无密访问
        '''
        self.work_threads = []
        self.work_num = 1
        self.number = len(self.desthost)

        if not os.path.isfile('/root/.ssh/id_rsa'):
            child01 = pexpect.spawn('/usr/bin/ssh-keygen -P "" -t rsa -f "/root/.ssh/id_rsa"')

        if self.number <10:
            self.work_num = self.number
        else:
            self.work_num = 10

        for index in range(1,self.work_num+1):
            th = threading.Thread(target=self.ssh_work,args=(index,))
            self.work_threads.append(th)

        for th in self.work_threads:
            th.start()

        for th in self.work_threads:
            threading.Thread.join(th)

#利用Socket进行端口扫描
class PortScanner(object):

    # default ports to be scanned
    # or put any ports you want to scan here!
    __port_list = [22,443,80,8181,8080,3306,5601,9600,9200,9300]
    # default thread number limit
    __thread_limit = 100
    # default connection timeout time inseconds
    __delay = 2

    def __init__(self, target_ports = None, target_ips = None):
        # If target ports not given in the arguments, use default ports
        # If target ports is given in the arguments, use given port lists
        if target_ports is None:
            self.target_ports = self.__port_list
        else:
            self.target_ports = target_ports

        if target_ips is None:
            self.target_ips = '127.0.0.1'
        else:
            self.target_ips = target_ips

    def __usage(self):
        print('python Port Scanner v0.1')

    #def scan(self, host_name, message = ''):
    def scan(self, message = ''):

        #if 'http://' in host_name or 'https://' in host_name:
        #    host_name = host_name[host_name.find('://') + 3 : ]

        ip_list = []
        try:
            #server_ip = socket.gethostbyname(str(host_name))
            for host_name in self.target_ips:
                if 'http://' in host_name or 'https://' in host_name:
                    host_name = host_name[host_name.find('://') + 3 : ]
                server_ip = socket.gethostbyname(str(host_name))
                ip_list.append(server_ip)

        except socket.error as e:
            # If the DNS resolution of a website cannot be finished, abort that website.

            #print(e)
            print('hostname %s unknown!!!' % host_name)

            self.__usage()

            return {}

            # May need to return specificed values to the DB in the future
        result = []
        start_time = time.time()
        for ip in ip_list:
            output = self.__scan_ports(ip, self.__delay, message)
            result.append(output)
        stop_time = time.time()

        #print('host %s scanned in  %f seconds' %(host_name, stop_time - start_time))

        #print('finish scanning!\n')

        return result

    def set_thread_limit(self, num):
        num = int(num)

        if num <= 0 or num > 50000:

            print('Warning: Invalid thread number limit! Please make sure the thread limit is within the range of (1, 50,000)!')
            print('The scanning process will use default thread limit!')

            return

        self.__thread_limit = num

    def set_delay(self, delay):

        delay = int(delay)
        if delay <= 0 or delay > 100:

            print('Warning: Invalid delay value! Please make sure the input delay is within the range of (1, 100)')
            print('The scanning process will use the default delay time')

            return

        self.__delay = delay

    def show_target_ports(self):
        print ('Current port list is:')
        print (self.target_ports)

    def show_delay(self):
        print ('Current timeout delay is :%d' %(int(self.__delay)))

    def __scan_ports_helper(self, ip, delay, output, message):

        '''
        Multithreading port scanning
        '''

        port_index = 0

        while port_index < len(self.target_ports):

            # Ensure that the number of cocurrently running threads does not exceed the thread limit
            while threading.activeCount() < self.__thread_limit and port_index < len(self.target_ports):

                # Start threads
                thread = threading.Thread(target = self.__TCP_connect, args = (ip, self.target_ports[port_index], delay, output, message))
                thread.start()
                port_index = port_index + 1

    def __scan_ports(self, ip, delay, message):

        output = {}
        thread = threading.Thread(target = self.__scan_ports_helper, args = (ip, delay, output, message))
        thread.start()
        scan_info = []
        # Wait until all port scanning threads finished
        while (len(output) < len(self.target_ports)):
            continue

        # Print openning ports from small to large
        for port in self.target_ports:
            result = {'ip':ip, 'port':str(port), 'state': output[port]}
            scan_info.append(result)
            #print(str(port) + ': ' + output[port] + '\n')

        #return output
        return scan_info

    def __TCP_connect(self, ip, port_number, delay, output, message):
        # Initilize the TCP socket object
        TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        TCP_sock.settimeout(delay)


        # Initilize a UDP socket to send scanning alert message if there exists an non-empty message
        if message != '':
            UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            UDP_sock.sendto(str(message), (ip, int(port_number)))

        try:
            result = TCP_sock.connect_ex((ip, int(port_number)))
            if message != '':
                TCP_sock.sendall(str(message))

            # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
            if result == 0:
                output[port_number] = 'OPEN'
            else:
                output[port_number] = 'CLOSE'

            TCP_sock.close()

        except socket.error as e:

            output[port_number] = 'CLOSE'
            pass

#压缩解压缩类
import zipfile
import os.path
import os
class ZFile(object):
  def __init__(self, filename, mode='r', basedir=''):
    self.filename = filename
    self.mode = mode
    if self.mode in ('w', 'a'):
      self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)
    else:
      self.zfile = zipfile.ZipFile(filename, self.mode)
    self.basedir = basedir
    if not self.basedir:
      self.basedir = os.path.dirname(filename)
  def addfile(self, path, arcname=None):
    path = path.replace('//', '/')
    if not arcname:
      if path.startswith(self.basedir):
        arcname = path[len(self.basedir):]
      else:
        arcname = ''
    self.zfile.write(path, arcname)
  def addfiles(self, paths):
    for path in paths:
      if isinstance(path, tuple):
        self.addfile(*path)
      else:
        self.addfile(path)
  def close(self):
    self.zfile.close()
  def extract_to(self, path):
    for p in self.zfile.namelist():
      self.extract(p, path)
  def extract(self, filename, path):
    if not filename.endswith('/'):
      f = os.path.join(path, filename)
      dir = os.path.dirname(f)
      if not os.path.exists(dir):
        os.makedirs(dir)
      file(f, 'wb').write(self.zfile.read(filename))
  '''
  使用方法如下：
  def create(zfile, files):
    z = ZFile(zfile, 'w')
    z.addfiles(files)
    z.close()
  def extract(zfile, path):
    z = ZFile(zfile)
    z.extract_to(path)
    z.close()
  '''

#操作redis 批量插入数据
class Redis_Handler(Handler):
	def connect(self):
		#print self.host,self.port,self.table
		self.conn = Connection(self.host,self.port,self.table)	
		
	def execute(self, action_name):
		filename = "/tmp/temp.txt"
		batch_size = 10000
		with open(filename) as file:
			try:
				count = 0
				pipeline_redis = self.conn.client.pipeline()
				for lines in file:
					(key,value) = lines.split(',')
						count = count + 1
						if len(key)>0:
							pipeline_redis.rpush(key,value.strip())
							if not count % batch_size:
								pipeline_redis.execute()
								count = 0
			
	
				#send the last batch
				pipeline_redis.execute()
			except Exception:
				print 'redis add error'
import hashlib                
#计算文件的md5
def sumfile(fobj):
    m = hashlib.md5()
    while True:
        d = fobj.read(8096)
        if not d:
            break
        m.update(d)
    return m.hexdigest()

def md5sum(fname):
    if fname == '-':
        ret = sumfile(sys.stdin)
    else:
        try:
            f = file(fname, 'rb')
        except:
            return 'Failed to open file'
        ret = sumfile(f)
        f.close()
    return ret

#redis 连接类
class redis_conn(object):
    def __init__(self, hostname="127.0.0.1", port='6379', db_num=0):
        self.hostname = hostname
        self.port = port
        self.db_num = db_num
    def conn_redis(self):
        pool = redis.ConnectionPool(host=self.hostname, port=self.port, db=self.db_num)
        rds = redis.Redis(connection_pool = pool)
        return rds
