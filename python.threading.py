#/usr/bin/python
#coding: utf-8
#
#
#	by wangdd 2016/08/29	


from atexit import register
from random import randrange
from threading import Thread,Lock,currentThread
from time import sleep,ctime


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

class CleanOutputSet(set):
	def __str__(self):
		return ','.join(x for x in self)

lock = Lock()
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

@register
def _atexit():
	print 'ALL Done at:',ctime()

if __name__ == '__main__':
	main()
