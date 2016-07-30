#-*- coding:utf8 -*-
#   by wangdd 2016/06/23

import re
import os,sys,time
import MySQLdb
import paramiko
import sys,os,time
import threading
import Queue

reload(sys)
sys.setdefaultencoding('utf8')
#------------------------------------------------------------
#定义了一个数据库操作类
class db_sql(object):

        """
        该类主要是用于对数据库操作时,处理sql语句
        """
        def db_connect(self,user,passwd,host,db_name,sql):
            '''
            定义了数据库连接
            '''
            self.sql = sql
            #self.param = param
            self.user = user
            self.db_name = db_name
            self.passwd = passwd
            self.host = host
            db = MySQLdb.connect(host,user,passwd,db_name,charset='utf8')
            #cursor()方法获取操作游标
            cursor = db.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            db.close()
            return result

        def safe(self,s):
            self.s = s
            return MySQLdb.escape_string(s)

        def get_i_sql(self,table,dict):
            '''
            生成insert的sql语句
            @table，插入记录的表名
            @dict,插入的数据，字典
            '''
            self.table = table
            self.dict = dict
            sql = 'insert into %s set ' % table
            sql += dict_2_str(dict)
            return sql


        def get_s_sql(self,table,keys,conditions=0,isdistinct=0,selecttype='accurate'):
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


        def get_u_sql(self,table,value,conditions):
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
            sql += dict_2_str(value)
            if conditions:
                sql += ' where %s ' % dict_2_str_and(conditions)
            return sql


        def get_d_sql(self,table, conditions):
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


        def dict_2_str(self,dictin):
            '''
            将字典变成，key='value',key='value' 的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ','.join(tmplist)


        def dict_2_str_and(self,dictin):
            '''
            将字典变成，key='value' and key='value'的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ' and '.join(tmplist)


        def dict_2_str_like(self,dictin):
            '''
            将字典变成，key like 'value' and key like 'value'的形式
            '''
            self.dictin = dictin
            tmplist = []
            for k, v in dictin.items():
                tmp = "%s like '%%%s%%'" % (str(k), self.safe(str(v)))
                tmplist.append(' ' + tmp + ' ')
            return ' and '.join(tmplist)

#------------------------------------------------------------
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
            rest = "----------------------------------------------------%s------------------------------------------------\n %s" % (hostname,out)
            ssh.close()
            self.q.put(rest)
        except Exception,e:
            return str(e)

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
