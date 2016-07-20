#!/bin/python
import sys,os
import MySQLdb
import paramiko
#come from caihw
#		if not os.path.isdir('/r2'):
#			print "Warning there is no /r2 dictroy"
#	def check_mysql(self):
#		if not os.path.isdir("/r2/mysqldata"):
#			print "please mkdir /r2/mysqldata"
if not os.path.isdir("/mysqlbackup"):
	os.mkdir("/mysqlbackup")
#		if os.popen("netstat -ntlp|grep 3306|wc -l").read.strip() = '0':			
#			os.popen("mysql_install_db")
#			os.popen("mysqld_safe &")
class mysqlconnect(object):
	def __init__(self):
		self.user='root'
		self.password='123456'
		self.databasepasswd='123456'
		self.port=22
		self.host1=sys.argv[1]
		self.host2=sys.argv[2]
	
	def export_table(self):
		s=paramiko.SSHClient()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(self.host1,self.port,self.user,self.password)
		conn1="mkdir /mastermysqlbackup"
		conn2='mysqldump -u%s -p%s --all-databases > /mastermysqlbackup/backupfirst.sql' % (self.user,self.databasepasswd)
		stdin,stdout,stderr=s.exec_command(conn1)
		stdin,stdout,stderr=s.exec_command(conn2)
		conn3='mysql -uroot -p123456 -e "show master status"'
		stdin,stdout,stderr=s.exec_command(conn3)
		result=stdout.readlines()[1].strip().split()
		binlog=result[0]
		log_pos=result[1]
		s.close()
		return binlog,log_pos

	def down_back(self):
#		os.popen("mkdir /mysqlbackup")
		local_dir='/mysqlbackup'
		remote_dir='/mastermysqlbackup'
		t=paramiko.Transport((self.host1,self.port))
		t.connect(username=self.user,password=self.password)
		sftp=paramiko.SFTPClient.from_transport(t)
		files=sftp.listdir(remote_dir)
		for f in files:
			sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))
	def check_slavemysql(self):
		s=paramiko.SSHClient()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(self.host2,self.port,self.user,self.password)
#			conn1="rm -rf /slavemysqlbackup"
		conn2="mkdir /slavemysqlbackup"
		stdin,stdout,stderr=s.exec_command(conn2)
		s.close()
	def up_back(self):
		local_dir='/mysqlbackup'
		remote_dir='/slavemysqlbackup'
		t=paramiko.Transport((self.host2,self.port))
		t.connect(username=self.user,password=self.password)
		sftp=paramiko.SFTPClient.from_transport(t)
		files=os.listdir(local_dir)
		for f in files:
			sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
		t.close()
	def import_date(self):
		s=paramiko.SSHClient()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		s.connect(self.host2,self.port,self.user,self.password)
		conn='mysql -u%s -p%s < /slavemysqlbackup/backupfirst.sql' % (self.user,self.databasepasswd)
		stdin,stdout,stderr=s.exec_command(conn)
#		result=stdout.readlines()
		s.close()
#		print result
	def slave_start(self):
		binlog,log_pos=self.export_table()
		
		sql="change master to master_host='%s',master_user='%s',master_password='%s',master_port=%s,master_log_file='%s',master_log_pos=%s;" % (self.host1,self.user,self.password,3306,binlog,log_pos)
		conn = MySQLdb.connect(host = self.host2,user = self.user,passwd = self.password,connect_timeout=5)  
		cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
		cursor.execute("slave stop;")
		cursor.execute(sql)
		cursor.execute("slave start;") 
#		cursor.execute("show slave status;")
		cursor.close()
		conn.close()
	def del_masterdir(self):
                s=paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                s.connect(self.host1,self.port,self.user,self.password)
		conn1="rm -rf /mastermysqlbackup"
#                conn2="mkdir /slavemysqlbackup"
                stdin,stdout,stderr=s.exec_command(conn1)
		s.close()
	def del_slavedir(self):
                s=paramiko.SSHClient()
                s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                s.connect(self.host2,self.port,self.user,self.password)
#                       conn1="rm -rf /slavemysqlbackup"
                conn1="rm -rf /slavemysqlbackup"
                stdin,stdout,stderr=s.exec_command(conn1)
		s.close()
	def del_localdir(self):
		os.popen("rm -rf /mysqlbackup")
boss=mysqlconnect()
boss.export_table()
boss.down_back()
boss.check_slavemysql()
boss.up_back()
boss.import_date()
boss.slave_start()
boss.del_masterdir()
boss.del_slavedir()
boss.del_localdir()
