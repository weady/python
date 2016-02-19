#!/usr/bin/python
# coding:utf-8
#
#这个脚本主要是对apache日志文件的处理分析,过滤出需要的信息
#处理后得到的数据是:	主机IP:192.168.14.44     访问流量:814 K
#使用说明 python 脚本名 文件名;  eg:python python.analysis.apachelog.py access.log
#
#	by wangdd 2016/02/02
#
import os
import re
import sys
import shelve

#re 模块,利用re模块对apahce日志进行分析
#通过 re.match(……) 和 re.compile(……).match返回
#    该对象有如下方法和属性：
#    方法：
#    group( [group1, ...])
#    groups( [default])
#    groupdict( [default])
#    start( [group])
#    end( [group]) 
#
# apache 日志格式: 192.168.47.82 - - [17/Dec/2014:16:41:03 +0800] "GET /application/account/loginIndex.htm HTTP/1.1" 200 56273
#
#基本思路是，利用re模块进行正则匹配，过滤出对应IP的访问字节数，然后把数据保存到apache_log.db数据库中，最后进行数据的格式

log_line_re = re.compile(r'''(?P<remote_host>^\d{1,3}\.(\d{1,3}\.){2}\d{1,3})
			     \s+
			     (?P<log_name>\S+)
			     \s+
			     (?P<login_user>\S+)
			     \s+
			     (?P<time>\[.*\])
		             \s+
 			     ".*"
			     \s+
			     (?P<status>\d+)
			     \s+
			     (?P<bytes_sent>-|\d+)
			''',re.X)
#利用正则表达过滤出需要的数据,返回一个字典类型的数据
def logline(line):
    m = log_line_re.search(line)
    if m:
	groupdict = m.groupdict()
	if groupdict['bytes_sent'] == '-':
		groupdict['bytes_sent'] = '0'
	return groupdict
    else:
	return {'remote_host':None,'status':None,'bytes_sent':"0",}
#从获取的字典中得到需要的数据
def log_report(logfile):
    report_dict ={}
    for line in logfile:
	line_dict = logline(line)
	try:
		bytes_sent = int(line_dict['bytes_sent'])
	except ValueError:
		continue
	report_dict.setdefault(line_dict['remote_host'],[]).append(bytes_sent)
    for k,v in report_dict.iteritems():
	sum = 0
	if k != None:
		for data in v:
			sum = sum +data
    		print '主机IP:%s\t 访问流量:%s K' % (k,sum/1024)

#这个函数是把处理后的数据保存到data.db文件中,利用了shelv 模块
def store_data(file):
    shelv_file = shelve.open('apache_log.db')
    if not os.path.isfile('shelv_file'):
    	for line in file:
		d_line = logline(line)
        	shelv_file[d_line['remote_host']] = \
                	shelv_file.setdefault(d_line['remote_host'],0) + \
                	int (d_line['bytes_sent'])
		data_file.close()
		shelv_file.close() 

if __name__ == '__main__':
    if not len(sys.argv) >1:
	print __doc__
	sys.exit(1)
    infile_name = sys.argv[1]
    try:
	infile = open(infile_name,'r')
    except IOError:
	print "please input some file"
	print __doc__
	sys.exit(1)
    log_report(infile)
    store_data(infile)
    infile.close()

#--------------------------------------------------------------------
