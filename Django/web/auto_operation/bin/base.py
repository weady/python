#-*- coding:utf8 -*-
#   by wangdd 2016/06/23

import re
import os,sys,time
import MySQLdb
#---------------------------------------------------------------
#主机管理模块中,通过/etc/hosts获取主机列表
def get_host_lists():
        file = open('/etc/hosts')
        names = file.read()
        m=re.findall(r"slave\d+$|redis\d+$|trans\d+$|record\d+$",names,re.MULTILINE)
        hostname = list(set(m))
        tem_list=['master','secondmaster']
        slave_list=[]
        redis_list=[]
        record_list=[]
        trans_list=[]
        file.close()
        for value in hostname:
                if re.search(r"slave\d+$",value):
                        slave_list.append(value)
                        slave_list.sort(key = lambda x:int(re.match('\D+(\d+)',x).group(1)))
                if re.search(r"redis\d+$",value):
                        redis_list.append(value)
                        redis_list.sort(key = lambda x:int(re.match('\D+(\d+)',x).group(1)))
                if re.search(r"record\d+$",value):
                        record_list.append(value)
                        record_list.sort(key = lambda x:int(re.match('\D+(\d+)',x).group(1)))
                if re.search(r"trans\d+$",value):
                        trans_list.append(value)
                        trans_list.sort(key = lambda x:int(re.match('\D+(\d+)',x).group(1)))

        host_lists=tem_list+slave_list+redis_list+record_list+trans_list
        return host_lists

#---------------------------------------------------------------
#从homed_iuds数据库的dns_domain_info表 domain_name,domain_info,domain_modified_time中查询云平台上域名信息
#连接数据库
def get_domain_info():
        file = open('/homed/allips.sh')
        data=file.read()
        host=re.findall(r'export iuds_mysql_ips="(.*)"',data,re.I)
        iuds_database="homed_iuds"
        user="root"
        passwd=re.findall(r'<mt_db_pwd>(\d+)',open('/homed/config_comm.xml').read(),re.I)
        db = MySQLdb.connect(host[0],user,passwd[0],iuds_database)
        #cursor()方法获取操作游标
        cursor = db.cursor()
        sql="select domain_name,domain_info,domain_modified_time from dns_domain_info"
        cursor.execute(sql)
        domain_info = cursor.fetchall()
        db.close()
        return domain_info


#---------------------------------------------------------------
#从auto_operation数据库中获取云平台的服务分布信息
def get_service_distribute():
        user="root"
        db_name="auto_operation"
        passwd="123456"
        host="192.168.36.108"
        db = MySQLdb.connect(host,user,passwd,db_name,charset='utf8')
        #cursor()方法获取操作游标
        cursor = db.cursor()
        sql="select cluster_name,hostname,server_name,server_id,status,server_function,note from t_service_distribution"
        try:
            cursor.execute(sql)
            service_distribute_info = cursor.fetchall()
            return service_distribute_info
        except Exception,e:
            return str(e)
        db.close()

