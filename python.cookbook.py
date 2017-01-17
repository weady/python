#!/usr/bin/python
#coding:utf8

#	by wangdd 2016/11/07
#这个文件主要记录学习pythoncookbook书时的学习笔记

#--------------------第一章----------------------------------
	collections.deque 双向队列,deque(maxlen=N)构造一个固定大小的队列,当新的元素加入并且这个队列已满的时候
	最老的元素会自动被移除掉
	q = deque(maxlen=3)
	q.append(1)
	如果你不设置最大队列大小那么就会得到一个无限大小队列你可以在队列的两端执行添加和弹出元素的操作
	q = deque()
	q.appendleft(4)	#队列左侧添加数据
	q.popleft()	#提出队列最左侧数据

	从一个集合中获取最大或最小的N个元素列表heapq 模块 nlargest() nsmallest()
	heap(0) 永远是最小的元素,并且剩余的元素可以很容易的通过调用 heapq.heappop() 方法得到
	该方法会先将第一个元素弹出来，然后用下一个最小的元素来取代被弹出元素
	获取唯一一个最大或最小的 使用min() max() 即可
	如果N的大小和集合大小接近的时候 通常先排序这个集合然后再使用切片操作会更快点 
	( sorted(items)[:N] 或者是 sorted(items)[-N:] )

	s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
	d = collections.defaultdict(list)
	for k, v in s:
    	d[k].append(v)
    
    使用 collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入时的顺序
    在一个字典上执行普通的数学运算，你会发现它们仅仅作用于键，而不是值
    获取字典中的最大值或最小值,利用zip() 对k,v进行反转然后利用max() 比较key 即可
    查找两个字典的相同点 可以使用集合操作的方式 & - ^
    a.keys() & b.keys() 发现字典a,b中的相同key
    a.keys() - b.keys() 发现在a中不在b中
    a.keys() ^ b.keys() 发现字典a,b 中的不同key
    a.items() & b.items() 发现字典中的相同(key,value)
    
    python 迭代器(iterator)
    for循环可用于任何“可迭代对象”，这其实就是迭代器
    迭代器是一个实现了迭代器协议的对象，Python中的迭代器协议就是有next方法的对象会前进到下一结果
    生成器(constructor)
    包含yield语句的函数会被特地编译成生成器,当函数被调用时,他们返回一个生成器对象
    这个对象支持迭代器接口。函数也许会有个return语句，但它的作用是用来yield产生值的
    不像一般的函数会生成值后退出,生成器函数在生成值后会自动挂起并暂停他们的执行和状态
    他的本地变量将保存状态信息,这些信息在函数恢复时将再度有效
    先yield来装入数据、产出generator object、使用next()来释放
    生成器函数 next()读取生成器数 send()可以向生成器传递参数
    使用生成器就不需要返回整个列表，每次都只是返回一个数据，避免了内存的限制问题

    内置的 slice() 函数创建了一个切片对象，可以被用在任何切片允许使用的地方
    a = slice(2, 4) items(a) == items[2:4]
    如果你有一个切片对象a，你可以分别调用它的 a.start , a.stop , a.step

    获取一个序列中重现次数最多的元素
    collections.Counter 类就是专门为这类问题而设计的， 它甚至有一个有用的 most_common() 方法
    from collections import Counter
    word_counts = Counter(words)
    # 出现频率最高的3个单词
    top_three = word_counts.most_common(3)
    print(top_three)
    查找两个字典的相同点(相同的键或者相同的值)
    # Find keys in common
    a.keys() & b.keys() # { 'x', 'y' }
    # Find keys in a that are not in b
    a.keys() - b.keys() # { 'z' }
    # Find (key,value) pairs in common
    a.items() & b.items() # { ('y', 2) }
    keys()键视图的一个很少被了解的特性就是它们也支持集合操作，比如集合并、交、差运算
    values()在值上面执行这些集合操作的话，你可以先将值集合转换成set，然后再执行集合运算就行了

    通过某个关键字排序一个字典列表
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname')) fname代表字典的key
    rows_by_fname = sorted(rows, key=lambda r: r['fname'])

    合并多个字典可以使用update() 或者使用collections 模块中的 ChainMap 类
    一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典然后
    这些字典并不是真的合并在一起了ChainMap 类只是在内部创建了一个容纳这些字典的列表
    并重新定义了一些常见的字典操作来遍历这个列表
    如果出现重复键，那么第一次出现的映射值会被返回。 
    因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值








#--------------------第二章----------------------------------
#--------------------第三章----------------------------------
#--------------------第四章----------------------------------
#--------------------第五章----------------------------------
#--------------------第六章----------------------------------
#--------------------第七章----------------------------------
#--------------------第八章----------------------------------
#--------------------第九章----------------------------------
#--------------------第十章----------------------------------
#--------------------第十一章----------------------------------
#--------------------第十二章 并发编程----------------------------------
'''
Python解释器直到所有线程都终止前仍保持运行
对于需要长时间运行的线程或者需要一直运行的后台任务你应当考虑使用后台线程
由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型
所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等
而不是需要多处理器并行的计算密集型任务
'''
from threading import Thread
t = Thread(target=countdown, args=(10,))
t.start() #启动线程
if t.is_alive(): #查看一个线程的状态
    print('Still running')
else:
        print('Completed')
t = Thread(target=countdown, args=(10,), daemon=True) #设定守护线程
t.start()