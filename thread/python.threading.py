#/usr/bin/python
#coding: utf-8
#
#
#	by wangdd 2016/08/29	


from atexit import register
from random import randrange
import threading
from time import sleep,ctime


#-----------------------------------------------------------------
#定义了一个类实现对threading模块的thread方法进行重写
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print 'Starting',self.name,'at:', ctime()
        self.res = self.func(*self.args)
        print self.name,'Finished at:',ctime()

#-----------------------------------------------------------------
class CleanOutputSet(set):
	def __str__(self):
		return ','.join(x for x in self)

lock = threading.Lock()
loops = (randrange(2,5) for x in xrange(randrange(3,7)))
remaining = CleanOutputSet()

#利用lock进行临界区管理
def loop(nsec):
	myname = currentThread().name
	lock.acquire()
	remaining.add(myname)
	print '[%s] Started %s' % (ctime(),myname)
	lock.release()
	sleep(nsec)
	lock.acquire()
	remaining.remove(myname)
	print '[%s] Completed %s (%d secs)' % (ctime(),myname,nsec)
	print '(remaining:%s)' % (remaining or 'NONE')
	lock.release()

#利用上下文管理进行临界区管理,使用with语句，此时每个对象的上下文管理器负责在进入该套件之前调用acquire()并在完成执行之后调用release()
def loop1(nsec):
	myname = currentThread().name
	with lock:
		remaining.add(myname)
		print '[%s] Started %s' % (ctime(),myname)
	sleep(nsec)
	with lock:
		remaining.remove(myname)
		print '[%s] Completed %s (%d sec)' % (ctime(),myname,nsec)
		print 'Remaining:%s' % (remaining or 'NONE')

def main():
	for pause in loops:
		Thread(target=loop1,args=(pause,)).start()

#使用atexit模块中的register方法,以便让解释器在脚本退出前执行该函数,无论改函数位于何处
@register
def _atexit():
	print 'ALL Done at:',ctime()

#-----------------------------------------------------------------
#生产者消费者模型
from random import randint
from time import sleep
from Queue import Queue

def writeQ(queue):
	print 'Producing object for Q....',
	queue.put('xxx',1)
	print 'size now',queue.qsize()

def readQ(queue):
	val = queue.get(1)
	print 'consumed object from Q.... size now',queue.qsize()

def writer(queue,loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1,3))

def reader(queue,loops):
	for i in range(loops):
		readQ(queue)
		sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main01():
	nloops = randint(2,5)
	q = Queue(32)

	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i],(q,nloops),funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()

	print 'all Done'

#---------------------------线程池模板---------------------------------
#线程池提供并发
import Queue
import threading
import time
class WorkManager(object):
    def __init__(self, work_num=1000,thread_num=2):
        self.work_queue = Queue.Queue()
        self.threads = []
        self.__init_work_queue(work_num)
        self.__init_thread_pool(thread_num)
    """
        初始化线程
    """
    def __init_thread_pool(self,thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))
    """
        初始化工作队列
    """
    def __init_work_queue(self, jobs_num):
        for i in range(jobs_num):
            self.add_job(do_job, i)
    """
        添加一项工作入队
    """
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))#任务入队，Queue内部实现了同步机制
    """
        检查剩余队列任务
    """
    def check_queue(self):
        return self.work_queue.qsize()
    """
        等待所有线程运行完毕
    """ 
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():item.join()
class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()
    def run(self):
        #死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                do, args = self.work_queue.get(block=False)#任务异步出队，Queue内部实现了同步机制
                do(args)
                self.work_queue.task_done()#通知系统任务完成
            except Exception,e:
                print str(e)
                break
#具体要做的任务
def do_job(args):
    print args
    time.sleep(0.1)#模拟处理时间
    print threading.current_thread(), list(args)
if __name__ == '__main__':
    start = time.time()
    work_manager =  WorkManager(10, 2)#或者work_manager =  WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print "cost all time: %s" % (end-start)

