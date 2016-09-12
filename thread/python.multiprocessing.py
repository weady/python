#!/usr/bin/python
#coding=utf8
#
#	by wangdd 2016/04/29
#


#-------------------01-------------------------------------------
#
import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

def test01():
    if __name__ == '__main__':
	jobs = []
	for i in range(5):
        	p = multiprocessing.Process(target=worker, args=(i,)) #启动多个进程
        	jobs.append(p)
        	p.start()

#-------------------02-------------------------------------------
#
import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name #获取进程的名字
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'

def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(3)
    print name, 'Exiting'

def test02():
    if __name__ == '__main__':
    	service = multiprocessing.Process(name='my_service',target=my_service)
   	worker_1 = multiprocessing.Process(name='worker 1',target=worker) #为进程定义名字
	worker_2 = multiprocessing.Process(target=worker) 

	worker_1.start() #启动进程
	worker_2.start()
	service.start()

#-------------------03-------------------------------------------
#
import os
import threading
import multiprocessing
 
# worker function
def worker(sign, lock):
    lock.acquire()
    print(sign, os.getpid())
    lock.release()

def test03():
    if __name__ == '__main__':
	# Main
	print('Main:',os.getpid())
 
	# Multi-thread
	record = []
	lock  = threading.Lock()
	for i in range(5):
	    thread = threading.Thread(target=worker,args=('thread',lock))
	    thread.start()
	    record.append(thread)
 
	for thread in record:
	    thread.join()
 
	# Multi-process
	record = []
	lock = multiprocessing.Lock()
	for i in range(5):
	    process = multiprocessing.Process(target=worker,args=('process',lock))
	    process.start()
	    record.append(process)
 
	for process in record:
	    process.join()

#-------------------04-------------------------------------------
#
import multiprocessing
import logging
import sys

def worker():
    print 'Doing some work'
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
