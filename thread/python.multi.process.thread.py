#/usr/bin/python
#coding=utf8
#
# 进程通信

import os,random,time
from multiprocessing import Pool, Queue, Process
import multiprocessing
import threading


#----------------------------------进程和进程池---------------------------------------------------------
def run_proc(name):
    print "Child process %s (%s) Running....." % (name,os.getpid())

def creat_process():
    print "Parent process %s " % os.getpid()
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))
        print "Process will start"
        p.start()

    p.join()
    print "Process end"

def run_pool_proc(name):
        print "task %s (pid = %s) is runngin.... " %(name,os.getpid())
        time.sleep(random.random() * 3)
        print 'task %s end' % name

def create_pool_process():
    print 'current process %s ' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_pool_proc,args=(i,))

    print 'waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'all subprocesses done'

#----------------------------------多进程---------------------------------------------------------
#进程池通信
def run_pool_pro(name):
    print 'task %s (pid=%s) is running....' % (name,os.getpid())
    time.sleep(random.random() * 3)
    print 'task %s end.' % name

def create_pool_pro():
    print 'current process %s' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_pool_pro,args=(i,))

    print 'waiting for all subprocesses done'
    p.close()
    p.join()
    print 'all subprocesses done'

#---------------------------------------------------------
#进程间通信 queue 队列 
#写进程
def proc_write(q,urls):
    print 'process (%s) is writing....' % os.getpid()
    for url in urls:
        q.put(url)
        print 'put %s to queue.....' % url
        time.sleep(random.random())


#读进程
def proc_read(q):
    print 'process (%s) is reading....' % os.getpid()
    while True:
        url = q.get(True)
        print 'get %s from queue' % url

def proc_queue():
    q = Queue()
    proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2 = Process(target=proc_write,args=(q,['url_4','url_5','url_6']))

    proc_reader = Process(target=proc_read,args=(q,))

    #启动写进程
    proc_writer1.start()
    proc_writer2.start()

    #启动读进程
    proc_reader.start()

    #等待写进程结束
    proc_writer1.join()
    proc_writer2.join()

    #读进程是死循环，无法等待其结束，只能强制终止
    proc_reader.terminate()

#进程间通信 pipe
def proc_pipe_send(pipe,urls):
    for url in urls:
        print "Process (%s) send: %s " % (os.getpid(),url)
        pipe.send(url)
        time.sleep(random.random())

def proc_pipe_recv(pipe):
    while True:
        print 'Process (%s) rev: %s' % (os.getpid(),pipe.recv())
        time.sleep(random.random())

def proc_pipe():
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_pipe_send,args=(pipe[0],['url_' + str(i) for i in range(10)]))

    p2 = multiprocessing.Process(target=proc_pipe_recv,args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.terminate()


#----------------------------------多线程---------------------------------------------------------
#
def thread_run_01(urls):
    print 'current %s is running...' % threading.current_thread().name
    for url in urls:
        print '%s ----> %s' % (threading.current_thread().name,url)
        time.sleep(random.random())
    print '%s ended' % threading.current_thread().name

def create_thread_01():
    print '%s is running...' % threading.current_thread().name
    t1 = threading.Thread(target=thread_run_01,name='Thread_01',args=(['url_01','url_02'],))

    t2 = threading.Thread(target=thread_run_01,name='Thread_02',args=(['url_03','url_04'],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print '%s ended' % threading.current_thread().name


#从threading.Thread继承创建线程类
class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls = urls

    def run(self):
        print 'current %s is running' % threading.current_thread().name
        for url in self.urls:
            print '%s ----> %s' % (threading.current_thread().name,url)
            time.sleep(random.random())
        
        print '%s ended' % threading.current_thread().name

def create_thread_02():
    print '%s is running...' % threading.current_thread().name
    t1 = myThread(name='Thread_01',urls=['url_01','url_02'])

    t2 = myThread(name='Thread_02',urls=['url_03','url_04'])

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print '%s ended' % threading.current_thread().name


if __name__ == '__main__':
    #create_pool_pro()
    #proc_queue()
    #proc_pipe()
    #create_thread_01()
    create_thread_02()

if __name__ == '__main__':
    create_pool_process()
