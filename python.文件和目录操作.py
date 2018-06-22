文件读写使用with..as 方式
如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore') encoding 指定读取文件的编码
linecache，这个模块也可以解决大文件读取的问题，并且可以指定读取哪一行
面对百万行的大型数据使用with open 是没有问题的，但是这里面参数的不同也会导致不同的效率。经过测试发先参数为"rb"时的效率是"r"的6倍
linecache 用以实现高效读取大文件内容或者需要经常访问的文件,linecache先把文件一次性读入到缓存中，在以后访问文件的时候，就不必要再从硬盘读取
lines = linecache.getlines(filename) 得到行列表，然后进行遍历读取
line = linecache.getline(filename,linenum)  读取指定行
