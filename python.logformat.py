#!/usr/bin/python
#coding:utf8
#  by wangdd 2017/02/20

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

import logging,os

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
		
		self.logger.addHandler(sh)
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

if __name__ == '__main__':
	loginfo = Logger('wangdong.log',logging.ERROR, logging.DEBUG)
	loginfo.debug('debug message')
	loginfo.info('info message')
	loginfo.warn('warn message')
	loginfo.error('error message')
