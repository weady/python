第一章
1.3.1
  1. 文件读写
    open(name[.mode[.buffering]])  文件名必须 mode 和缓存可选  默认读模式，默认缓存区无
  2.文件模式
    r w a b + 参数rb 用来读去一个二进制文件
  3.文件缓冲区
    open函数的第三个参数buffering  控制着文件的缓冲
    0: I/O 无缓冲，直接落盘
    1: I/O 有缓冲，数据先写入内存，只有使用flush 或　close 函数数据才落盘
    大于1 表示缓冲区的大小单位字节
    -1 代表使用默认缓冲区的大小
  4.文件读取
    文件读取主要分为按字节读取和按行进行读取，经常使用的方法有read() readlines() close()
    with open(xxx) as file:
    print file.read()
    read()  方法可以一次把文件内容全部读到内存中，返回str 类型的对象
    read(size) 大文件可以反复调用　read(size)方法，一次最多读取size   个字节
    readline() 每次读取一行内容
    readlines() 一次读取所有内容并按行返回列表
    小文件直接采用read()
    大文件采用read(size)
    配置文件等文本文件 采用readline() 或readlines()
    5.文件写入
      写文件和读取文件唯一的区别是调用open方法时，传入标识符'w'或者'wb' 表示写入文件文件或者写入二进制文件
      write() 方法的时候，操作系统不会立刻将数据写入文件中，而是先写入内存缓存起来，等空闲时再写入文件中，最后使用close() 方法将数据写入文件中。也可以使用f.flush()方法，不断将数据立即写入文件中，最后使用close()方法关闭文件
      使用with open() as filewriter:
1.3.2 操作文件和目录
  python 中对文件和目录的操作使用 os  和shutil 模块
  shutil.copytree('olddir','newdir')  复制目录，newdir必须不存在
  shutil.copyfile('oldfile','newfile') 文件复制
  shutil.move('oldpos','newpos') 移动文件(目录)
  os.rmdir('dir') 只能删除空目录
  shutil.rmtree('dir') 空目录，有内容的目录都可以删
1.3.3 序列化操作
  把内存中的变量变成可存储或可传输的过程，就是序列化。把变量内容从序列化的对象重新读取到内存称为反序列化
  cPickle pickle
  try:
  import cPickle as pickle
  except ImportError:
  import pickle

  pickle 实现序列化主要使用的是dumps 或dump 方法。 
  dumps() 方法可以将任意对象序列化成一个str放入内存，然后通过loads()进行从内存中反序列化。也可以将这个str写入文件进行保存。
  dump()  直接将这个str写入文件进行保存  pickle.dump(obj,file),使用pickle.load(file) 直接把文件反序列化
  dumps()  序列化到内存，对应的反序列化 loads()
  dump() 序列化到文件，对应的反序列化load()
1.4 进程和线程
  python 实现多进行的方式主要有两种，一种是使用 os 模块中的fork 方法，另外一种是使用multiprocessing模块。
  fork 方法调用一次，返回两次。操作系统将当前进程(父进程)复制出一份进程(子进程)，两个进程几乎完成相同，fork 方法在父进程和子进程中返回，子进程中永远返回0，父进程中返回的是子进程的id。
  使用multiprocessing 模块创建多进程，mutiprocessing 模块提供了一个process类来描述一个进程对象，创建子进程只需要传入一个执行函数和函数的参数，即可完成一个process 实例的创建。用start()方法启动，用join()  实现进程间
  进程池，multiprocessing 提供了一个Pool类来代表进程池对象，默认为cpu核数。当一个任务结束了，新的任务一次添加进来，任务执行使用的进程依然是原来的进程。Pool 对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close(),调用close()之后就不能继续添加新的Process了
  进程间通信
  python提供了多种进程间通信方式 queue pipe 等。queue 和pipe 的区别在于pipe常用来在两个进行间通信，queue 在多个进程间实现通信
  queue 是多进程安全的队列，可以使用queue实现多进程之间的数据传递。有两个方法:put和get 可以进行queue操作
  put 方法用于插入数据到队列中，两个可选参数:blocked 和timeout。blocked 默认为ture，timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。超时抛出queue.full异常。
  get 方法从队列中读取并删除一个元素。两个可选参数blocked timeout。参数原理同put方法
  pip 通过用来在两个进程间进行通信,两个进程分别位于管道的两端
  pip 方法返回(conn1,conn2) 代表一个管道的两端。pipe 方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道为全工模式
  conn1 和conn2 均可收发。duplex 为false，conn1负责收，conn2负责发。send 和recv表示发送和接受消息。
  全双工模式下，可以调用conn1.send 发送消息，conn1.recv 接收消息。如果没有消息可接收，recv方法会一直阻塞。管道已经关闭，recv会抛出EOFError。
  多线程
  多线程的标准模块thread 和threading 
  threading 模块创建多线程
  第一种方式把一个函数传入并创建Thread实例，然后调用start方法开始执行；
  第二种方式直接从threading.Thread继承并创建线程类，然后重写__init__方法和run方法
















