#!/usr/bin/python
#coding:utf-8
import MySQLdb
def com_mysql():
#连接数据库
    db = MySQLdb.connect("192.168.36.130","root","123456","zabbix")
#cursor()方法获取操作游标
    cursor = db.cursor()
#执行sql语句
    cursor.execute("select version()")
#使用fetchone()方法获取一条数据
    data = cursor.fetchone()
    print "Database version is %s" % data
#--------------数据库建表---------------------------------------
    cursor.execute("drop table if exists wangdong")
    sql = """create table wangdong (
	id int,
	name varchar(10))"""
    cursor.execute(sql)
#--------------数据库插入操作-----------------------------------
    sql = """insert into wangdong 
	values (1,"wangdong")"""
    try:
	#执行sql语句
	cursor.execute(sql)
	#提交到数据库执行
	db.commit()
    except Exception as e:
	#rollback 以防有错误
        print e
	db.rollback()
    db.close()
#com_mysql()
#------------慕课网学习------------------------------------------
def mysql_python():
    conn = MySQLdb.Connect( host = '127.0.0.1',port = 3306,user = 'root',passwd = '123456',db = 'zabbix',charset = 'utf8')
    cursor = conn.cursor()
    sql = """show tables"""
    cursor.execute(sql)
    data = cursor.fetchone() #取出一条数据
    print data

    data = cursor.fetchmany(2)
    print data

    data = cursor.fetchall() #获取所有数据
    for row in data: #遍历数据
       print "Table name = %s" % row
    print cursor.rowcount #打印受影响的行数
    cursor.close()
    conn.close()
mysql_python()
