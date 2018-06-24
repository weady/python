文件读写使用with..as 方式
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore') encoding 指定读取文件的编码
linecache，这个模块也可以解决大文件读取的问题，并且可以指定读取哪一行
面对百万行的大型数据使用with open 是没有问题的，但是这里面参数的不同也会导致不同的效率。经过测试发先参数为"rb"时的效率是"r"的6倍
linecache 用以实现高效读取大文件内容或者需要经常访问的文件,linecache先把文件一次性读入到缓存中，在以后访问文件的时候，就不必要再从硬盘读取
lines = linecache.getlines(filename) 得到行列表，然后进行遍历读取
line = linecache.getline(filename,linenum)  读取指定行
file() 函数用于创建一个 file 对象，它有一个别名叫 open()
import cPickle as p 利用cPickle模块进行文件的存储读取
f = file(shoplistfile, 'w')  p.dump(shoplist, f)  f.close() dump数据到文件
f = file(shoplistfile) storedlist = p.load(f) print storedlist  load 数据从文件
不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法
F.read([size]) #size为读取的长度，以byte为单位 
F.readline([size]) #读一行，如果定义了size，有可能返回的只是一行的一部分 
F.readlines([size]) #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。 
F.write(str) #把str写到文件中，write()并不会在str后加上一个换行符 
F.writelines(seq) #把seq的内容全部写到文件中。这个函数也只是忠实地写入，不会在每行后面加上任何东西
用w或a模式打开文件的话，如果文件不存在，那么就自动创建。用w模式打开一个已经存在的文件时，原有文件的内容会被清空，因为一开始文件的操作的标记是在文件的开头的，这时候进行写操作，无疑会把原有的内容给抹掉
用U模式打开文件，就是支持所有的换行模式
F.tell() #返回文件操作标记的当前位置，以文件的开头为原点
F.seek(offset[,whence]) #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。 
r 只读 r+  读写 w  写入,先删除源文件,在重新写入,如果文件没有则创建 w+  读写,先删除源文件,在重新写入,如果文件没有则创建(可以写入写出)





