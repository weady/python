#/usr/bin/python
#coding=utf8
#
# 进程通信

import os,random,time
from multiprocessing import Pool, Queue, Process
import multiprocessing
import threading

‘’‘
    Queue的功能是将每个核或线程的运算结果放在队里中，等到每个线程或核运行完毕后再从队列中取出结果
    继续加载运算。原因很简单，多线程调用的函数不能有返回值，所以使用Queue存储多个线程运算的结果
    pool = mp.Pool()
    有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。
    Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值
    接下来用map()获取结果，在map()中需要放入函数和需要迭代运算的值
    Pool默认大小是CPU的核数，我们也可以通过在Pool中传入processes参数即可自定义需要的核数量
    pool = mp.Pool(processes=3)
    res = pool.map(job, range(10))
    print(res)
    apply_async()中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的
    所以在传入值后需要加逗号, 同时需要用get()方法获取返回值
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])
    共享内存：
    import multiprocessing as mp
    value1 = mp.Value('i', 0) 
    value2 = mp.Value('d', 3.14)
    其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型
    array = mp.Array('i', [1, 2, 3, 4]) 一维数组
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    l.acquire() # 锁住
    do something
    l.release() # 释放
    线程模块常用函数:
    threading.active_count() #活跃线程数
    threading.enumerate() #线程信息
    threading.current_thread() #当前线程
    add_thread = threading.Thread(target=thread_job,)   # 定义线程 
    add_thread.start() #启动线程
    add_thread.join() #主线程等待子线程全部运行完后才开始运行
    q.get() #从队列中获取值

    lock在不同线程使用同一共享内存时，能够确保线程之间互不影响，使用lock的方法是
    在每个线程执行运算修改共享内存之前，执行lock.acquire()将共享内存上锁
    确保当前线程执行时，内存不会被其他线程访问，执行运算完毕后，使用lock.release()将锁打开
    保证其他的线程可以使用该共享内存
’‘’
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
