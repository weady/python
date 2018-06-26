Gpip是一个安装和管理python包的工具
安装pip 下载软件包，然后运行python setup.py install即可
利用pip管理软件包
pip install fabric 
if _fastmath is not None and not _fastmath.HAVE_DECL_MPZ_POWM_SEC:
AttributeError: 'module' object has no attribute 'HAVE_DECL_MPZ_POWM_SEC'
pip install pycrypto-on-pypi
交互式编程:
python
>>>print "Hello world";
2.7.6以上的版本就需要使用print ("Hello world");
Python标识符
在python里，标识符有字母、数字、下划线组成
在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
python中的标识符是区分大小写的。
以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数
Python保留字符
这些保留字不能用作常数或变数，或任何其他标识符名称,所有Python的关键字只包含小写字母
and	exec	not  assert	finally	or  break	for	pass  class	from	print continue	global	raise 
def	if	return  del	import	try  elif	in	while else	is	with except	lambda	yield
行和缩进
学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行
多行语句
Python语句中一般以新行作为为语句的结束符。
但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
 total = item_one + \
        item_two + \
        item_three
语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
 days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
Python 引号
Python 接收单引号(' )，双引号(" )，三引号(''' """) 来表示字符串，引号的开始与结束必须的相同类型的。
其中三引号可以由多行组成，编写多行文本的快捷语法，常用语文档字符串，在文件的特定地点，被当做注释。
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
Python空行
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分
Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。
如下实例：
if expression :
   suite
elif expression :  
   suite  
else :  
   suite
多个变量赋值
Python允许你同时为多个变量赋值。例如：
a = b = c = 1
以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "john"
以上实例，两个整型对象1和2的分配给变量a和b，字符串对象"john"分配给变量c
Python有五个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dirctionary（字典）
python数字
Python支持四种不同的数值类型：
    int（有符号整型）
    long（长整型[也可以代表八进制和十六进制]）
    float（浮点型）
    complex（复数）
    长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
    Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
Python字符串
它是编程语言中表示文本的数据类型
python的字串列表有2种取值顺序:
    从左到右索引默认0开始的，最大范围是字符串长度少1
    从右到左索引默认-1开始的，最大范围是字符串开头
如果你的实要取得一段子串的话，可以用到变量[头下标:尾下标]，就可以截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾
字符串或串(String)是由数字、字母、下划线组成的一串字符。
加号（+）是字符串连接运算符，星号（*）是重复操作。如下实例：
#!/usr/bin/python
str = "Hello World!"
print str # 输出完整字符串
print str[0] # 输出字符串中的第一个字符
print str[2:5] # 输出字符串中第三个至第五个之间的字符串
print str[2:] # 输出从第三个字符开始的字符串
print str * 2 # 输出字符串两次
print str + "TEST" # 输出连接的字符串
以上实例输出结果：
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
Python列表 [ ]
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
列表中的值的分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：
#!/usr/bin/python
List = [ "abcd", 786 , 2.23, "john", 70.2 ]
tinylist = [123, "john"]
print List # 输出完整列表
print List[0] # 输出列表的第一个元素
print List[1:3] # 输出第二个至第三个的元素
print List[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print List + tinylist # 打印组合的列表
以上实例输出结果：
["abcd", 786, 2.23, "john", 70.200000000000003]
abcd
[786, 2.23]
[2.23, "john", 70.200000000000003]
[123, "john", 123, "john"]
["abcd", 786, 2.23, "john", 70.200000000000003, 123, "john"]
sorted(list)返回一个对象，可以用作表达式。原来的list不变，生成一个新的排好序的list对象。
list.sort() 不会返回对象，改变原有的list
对第二个关键字排序
>>>L = [('b',6),('a',1),('c',3),('d',4)]
>>>L.sort(key=lambda x:x[1])
 extend()和加号+连接操作符的区别
list1 + list2虽然看上去显示的结果和extend方法一样，但其实它得到的是一个新列表
extend方法是把元素添加到了list1中，相当于扩展（修改）list1的数据，但id没有改变。如果用+号连接的话，它返回的是一个新生成的列表
append列表添加方法被调用后，返回的列表不仅仅是一个添加过元素后的新列表，而是把原有的列表做了修改，id不变。并且新添加的元素是追加到原列表数据的末尾，append方法也被叫做列表追加操作
用列表的index()方法查找参数时：如果参数存在，返回索引位置；如果参数不存在，则报错
列表名.index('值') 返回值的索引下标值
与列表extend()追加方法和python append不同，insert()方法是可以将要添加的对象，插入到指定的位置中。
list.insert(3,'abc')
列表推导式标准格式
[Expression for Variable in  list]
也就是：[ 表达式  for  变量 in 列表]
如果需要加入if条件语句则是：[表达式 for 变量 in 列表 if 条件]
>>> a = [1,2,3,4,5,6,7,8,9,10]
>>> [3*x for x in a]
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
列表排序
sort()是python列表排序方法，除了列表cmp()比较函数可以做为参数放在sort()，key和reverse更是经常用到的sort方法另外两个可选参数
在很多情况下cmp参数可以用于sort和sorted函数，在排序时使用cmp()方法是非常有用的
>>> num = [6,3,8,7]
>>> num.sort(cmp)
x.sort(key=len)    //根据元素的长度进行排序
sort(key=int,reverse=True)    //以整型数字来排序，倒序
Python元组 ( )
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
#!/usr/bin/python
Tuple = ( "abcd", 786 , 2.23, "john", 70.2 )
tinytuple = (123, "john") 
print Tuple # 输出完整元组
print Tuple[0] # 输出列表的第一个元素
print Tuple[1:3] # 输出第二个至第三个的元素
print Tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print Tuple + tinytuple # 打印组合的元组
以上实例输出结果：
("abcd", 786, 2.23, "john", 70.200000000000003)
abcd
(786, 2.23)
(2.23, "john", 70.200000000000003)
(123, "john", 123, "john")
("abcd", 786, 2.23, "john", 70.200000000000003, 123, "john")
以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：
#!/usr/bin/python
Tuple = ( "abcd", 786 , 2.23, "john", 70.2 )
List = [ "abcd", 786 , 2.23, "john", 70.2 ]
Tuple[2] = 1000 # 错误！元组中是非法应用
List[2] = 1000 # 正确！列表中是合法应用
list(Tuple)    //把元组转换为列表
tuple(List)    //把列表转换为元组
列表的pop()方法，是python 列表类型的内建函数，主要用来做删除列表中的指定对象（如果没有指定对象，默认是最后一个值）
一般删除对象方法会直接将元素删除，而pop()方法在删除指定对象时，会返回要删除元素的值。可以理解为一个提示作用，提示你删除的是哪一个元素
pop()括号内参数是，要删除对象的python list 索引。如果为空则默认为-1最后一项
Python元字典 { }
字典get()方法，可以访问字典中键对应的值。key存在则返回对应value，键不存在返回None，也可以设定自己的返回参数，设置的方法是：变量名.get（键名,参数）
字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典用"{ }"标识。字典由索引(key)和它对应的值value组成
字典删除方法：clear()、pop()和popitem()
clear()方法是用来清除字典中的所有数据，因为是原地操作，所以返回None（也可以理解为没有返回值）
dict.clear()
移除字典数据pop()方法的作用是：删除指定给定键所对应的值，返回这个值并从字典中把它移除
dict.pop('key')
字典popitem()方法作用是：随机返回并删除字典中的一对键和值（项）
dict.popitem()
#!/usr/bin/python
dict = {}
dict["one"] = "This is one"
dict[2] = "This is two"
tinydict = {"name": "john","code":6734, "dept": "sales"}  
print dict["one"] # 输出键为"one" 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值
tinydict.items() 生成一个字典容器
print tinydict.copy()    生成字典副本
print tinydict.get('key')    访问字典项的方法
tinydict.update(d2)    合并字典
字典的删除: tinydict.pop('key')    del tinydict['key']
[('dept', 'sales'), ('code', 6734), ('name', 'john')]
输出结果为：
This is one This is two {"dept": "sales", "code": 6734, "name": "john"} ["dept", "code", "name"] ["sales", 6734, "john"]
python字典的items方法作用：是可以将字典中的所有项，以列表方式返回
字典.iteritems()方法在需要迭代结果的时候使用最适合，而且它的工作效率非常的高
字典遍历的方法:
aDict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print '-----------dict-------------'
for d in aDict:
    print "%s:%s" %(d, aDict[d])

print '-----------item-------------'
for (k,v) in aDict.items():
    print '%s:%s' %(k, v)
#效率最高
print '------------iteritems---------'
for k,v in aDict.iteritems():
    print '%s:%s' % (k, v)
#最笨的方法
print '---------iterkeys---------------'
for k in aDict.iterkeys():
    print '%s:%s' % (k, aDict[k])

print '------------iterkeys, itervalues----------'
for k,v in zip(aDict.iterkeys(), aDict.itervalues()):
    print '%s:%s' % (k, v)
Python 字典(Dictionary) setdefault() 函数和get()方法类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值
dict.setdefault(key, default=None)
    key -- 查找的键值。
    default -- 键不存在时，设置的默认键值
该方法没有任何返回值
dictMerged3 = dict1.copy()
dictMerged3.update( dict2 )
setdefault()方法和字典的get()方法在一些地方比较相像，都可以得到给定键对应的值。但setdefault()方法可以在字典中并不包含有给定键的情况下，为给定键设定相应的值
a.setdefault('name','lili')    #因为键名name存在，则返回键对应的值‘amy’
'amy'
>>> a.setdefault('name1','lili')  #因键名name1不存在，程序把('name1','lili')当做项添加到字典a中，并返回其值。
'lili'
Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可
str(x)    将对象 x 转换为字符串
list(s)    将序列 s 转换为一个列表
dict(d)    创建一个字典。d 必须是一个序列 (key,value)元组。
repr(x)    将对象 x 转换为表达式字符串
Python语言支持以下类型的运算符:
    算术运算符
+ - * / % ** //
**	幂 - 返回x的y次幂	a**b 输出结果 20
//	取整除 - 返回商的整数部分	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
    比较（关系）运算符
==    =!    <>    >    <    >=    <=
    赋值运算符
=    +=    -= *= /=    %=    **=    //=
    逻辑运算符
and or not
    位运算符
    成员运算符
    身份运算符
    运算符优先级
Python成员运算符
Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组
in	如果在指定的序列中找到值返回True，否则返回False
not in	如果在指定的序列中没有找到值返回True，否则返回False
常用函数
rang()
>>> range(1,5) #代表从1到5(不包含5)
[1, 2, 3, 4]
>>> range(1,5,2) #代表从1到5，间隔2(不包含5)
[1, 3]
>>> range(5) #代表从0到5(不包含5)
[0, 1, 2, 3, 4]
再看看list的操作:
array = [1, 2, 5, 3, 6, 8, 4]
#其实这里的顺序标识是
[1, 2, 5, 3, 6, 8, 4]
(0，1，2，3，4，5，6)
(-7,-6,-5,-4,-3,-2,-1)   
>>> array[0:] #列出0以后的
[1, 2, 5, 3, 6, 8, 4]
>>> array[1:] #列出1以后的
[2, 5, 3, 6, 8, 4]
>>> array[:-1] #列出-1之前的
[1, 2, 5, 3, 6, 8]
>>> array[3:-3] #列出3到-3之间的
[3]
那么两个[::]会是什么那？
>>> array[::2]
[1, 5, 6, 4]
>>> array[2::]
[5, 3, 6, 8, 4]
>>> array[::3]
[1, 3, 4]
>>> array[::4]
[1, 6]
如果想让他们颠倒形成reverse函数的效果
>>> array[::-1]
[4, 8, 6, 3, 5, 2, 1]
>>> array[::-2]
[4, 6, 5, 1]
len()
str = "this is string example....wow!!!";
print "字符串长度: ", len(str);
if 判断条件：
    执行语句……
else：
    执行语句……
多条件可以使用or and
while循环可以使用else
break跳出循环体      continue 跳出本次循环     pass是空语句，是为了保持程序结构的完整性
pass就是什么也不做，只是为了防止语法错误，比如：
if a>1:
    pass #我这里先不做任何处理，直接跳过，但是如果不写pass，就会语法错误
Python 数字数据类型用于存储数值。
数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
以下实例在变量赋值时数字对象将被创建：
var =1 
var =10
可以使用del语句删除一些数字对象引用
del var
del var_a, var_b
python 字符串
创建字符串
var1 = 'Hello World!'
var2 = "Python Programming"
python可以使用[]截取字符串
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
以上实例执行结果：
var1[0]:  H
var2[1:5]:  ytho
python转义字符 \
在行尾表示 续行符
字符串运算符
实例变量a值为字符串"Hello"，b变量值为"Python" 
+ 字符串连接    a + b 输出 hello python
* 重复输出字符串 a*2 输出hello hello 
[] 通过索引获取字符中的字符    a[1] 输出e
[:] 截取字符串的一部分    a[1:4] 输出 ell
in/not in 成员运算符   H in a 结果为1 判断某个字符是否在字符串中，在为真 1，不在为假 0
r/R 原样字符串 print r'\n 换行'
% 格式化字符串
print "My name is %s and weight is %d kg!" % ('Zara', 21) 
常用的字符串格式符 %s %d %f %c 
list 中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
使用del 可以直接删除列表中的某个值
del list1[0]    //把列表中的第一个值删除了
list脚本操作符
len([1,2,3])    计算列表的长度 3
[1,2]+[3,4] [1,2,3,4] 组合
['hi']*4 重复4次 hi hi hi hi 
3 in [1,2,3]
列表的截取
L = ['spam', 'Spam', 'SPAM!']
L[2]    读取列表中的第三个元素
L[-2]    读取列表中倒数第二个元素
L[1:]    从第二个元素开始截取
cmp(list1,list2)    比较两个列表的元素
len(list) 列表元素个数
max(list) 列表中最大值
min(list) 类别中最小值
list.append('test')    在列表末尾添加新的对象
list.count('test') 统计某个元素在列表中出现的次数
list.extend(seq) 在列表末尾一次性追加另外一个序列中的多个值
extend方法可以在列表尾部追加包含多个值的另一个序列，而list的append()只能添加一个值
list.index('test') 从列表中找出某个值第一个匹配项的索引位置
list.insert(index,'test') 将对象插入列表
list.pop([index]) 移除列表中的一个元素(默认最后一个元素)，并返回该元素的值
list.remove('test') 移除列表中某个值的第一个匹配项
list.reverse() 反向列表中的元素
list.sort([func]) 对原列表进行排序
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
创建空元组 tup1 = ();
元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,);
元组与字符串类似，下标索引从0开始，可以进行截取，组合等
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合 使用+
元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组
for x in (1, 2, 3): print x,	1 2 3	迭代
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
任意无符号的对象，以逗号隔开，默认为元组
x, y = 1, 2;
print "Value of x , y : ", x,y;
元组内置函数
cmp(a,b) 比较两个元组元素
len(a) 计算元组元素个数
max(tuple) min(tuple)
tuple(seq) 将列表转化为元组
字典是另一种可变容器模型，且可存储任意类型对象，如其他容器模型
字典由键和对应值成对组成。字典也被称作关联数组或哈希表。基本语法如下：
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
每个键与值用冒号隔开（:），每对用逗号，每对用逗号分割，整体放在花括号中（{}）。
键必须独一无二，但值则不必。
值可以取任何数据类型，但必须是不可变的，如字符串，数或元组
把相应的键放入熟悉的方括弧，就可以获取字典中的值
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ", dict['Name'];
修改字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};    
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典
不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
import time;  # This is required to include time module.
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()
localtime = time.asctime( time.localtime(time.time()) )
Calendar模块有很广泛的方法用来处理年历和月历
模块
模块的引入使用import time;
日历（Calendar）模块
星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数
time 模块，对时间的处理
datetime 模块，使用strftime格式化时间
pytz 模块
ateutil 模块
函数
自定义函数
函数代码块以def关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。 
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。 
函数内容以冒号起始，并且缩进。 
Return[expression]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
def 函数名( 参数 ):
   function_suite
   return [expression] 
函数调用
# Now you can call printme function
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");
用函数时可使用的正式参数类型：
必备参数
必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
命名参数
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
 
#调用printinfo函数
printinfo( age=50, name="miki" )
缺省参数 调用函数时，缺省参数的值如果没有传入，则被认为是默认值
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print "Name: ", name
   print "Age ", age
 
#调用printinfo函数
printinfo( age=50, name="miki" )
printinfo( name="miki" )
不定长参数 
加了星号（*）的变量名会存放所有未命名的变量参数
#!/usr/bin/python
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
匿名函数
用lambda关键词能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤
匿名函数不能直接调用print，因为lambda需要一个表达式
lambda函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
#!/usr/bin/python    
#可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
#调用sum函数
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )
变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
模块就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码
想使用Python源文件，只需在另一个源文件里执行import语句，语法如下：
import module1[, module2[,... moduleN]
如想要导入模块hello.py，需要把命令放在脚本的顶端
一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
from modname import name1[, name2[, ... nameN]]
例如，要导入模块fib的fibonacci函数，使用如下语句：
from fib import fibonacci
这个声明不会把整个fib模块导入到当前的命名空间中，它只会将fib里的fibonacci单个引入到执行这个声明的模块的全局符号表。
定位模块
当你导入一个模块，Python解析器对模块位置的搜索顺序是：
    当前目录
    如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录
    如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
模块搜索路径存存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
一个Python表达式可以访问局部命名空间和全局命名空间里的变量。如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量
Python会智能地猜测一个变量是局部的还是全局的，它假设任何在函数内赋值的变量都是局部的
dir()函数一个排好序的字符串列表，内容是一个模块里定义过的名字
特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名
globals()和locals()函数
根据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用keys()函数摘取
reload()函数
如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。语法如下：
reload(module_name)
Python中的包
包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的Python的应用环境。
最简单的输出方法是用print语句，你可以给它传递零个或多个用逗号隔开的表达式。此函数把你传递的表达式转换成一个字符串表达式，并将结果写到标准输出如下：
读取键盘输入
 Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：
    raw_input
    input
 input([prompt]) 函数和raw_input([prompt]) 函数基本可以互换，但是input会假设你的输入是一个有效的Python表达式，并返回运算结果。
#!/usr/bin/python
str = input("Enter your input: ");
print "Received input is : ", str
这会产生如下的对应着输入的结果：
Enter your input: [x*5 for x in range(2,10,2)]
Recieved input is :  [10, 20, 30, 40]
打开和关闭文件
 open函数
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的辅助方法才可以调用它进行读写。
语法：
file object = open(file_name [, access_mode][, buffering])
各个参数的细节如下：
    file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
    access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
打开的模式: r r+ rb rb+ w w+wb+ a a+ ab+
'r'->只读
'w'->只写，文件已存在则清空，不存在则创建。
'a'->追加，写到文件末尾
'b'->二进制模式,比如打开图像、音频、word文件，不要理由b打开文本文件
'+'->更新(可读可写)
f.write('Hello,World') 写入文件

File对象的属性
file.closed	返回true如果文件已被关闭，否则返回false。
file.mode	返回被打开文件的访问模式。
file.name	返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。
如下实例：
#!/usr/bin/python   
# 打开一个文件
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
以上实例输出结果：
Name of the file:  foo.txt
Closed or not :  False
Opening mode :  wb
Softspace flag :  0
Close()方法 关闭一个文件
Write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字
#!/usr/bin/python
# 打开一个文件
fo = open("/tmp/foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");
# 关闭打开的文件
fo.close()
read（）方法从一个打开的文件中读取一个字符串
 文件位置：
Tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后：
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。 
 Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
要使用这个模块，你必须先导入它，然后可以调用相关的各种功能。
rename()方法：
rename()方法需要两个参数，当前的文件名和新文件名
语法：
os.rename(current_file_name, new_file_name)
remove()方法
你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
语法：
os.remove(file_name)
mkdir()方法    os.mkdir("newdir")
chdir()方法    os.chdir("newdir") 
getcwd()方法显示当前的工作目录    os.getcwd()
 rmdir()方法删除目录，目录名称以参数传递。 os.rmdir('dirname') 在删除这个目录之前，它的所有内容应该先被清除
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序
异常处理
断言(Assertions)
捕捉异常可以使用 try/except 语句
try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()
使用except而不带任何异常类型 ,你可以不带任何异常类型使用except
使用except而带多种异常类型
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码
try:
<语句>
finally:
<语句>    #退出try时总会执行
raise
注意：你可以使用except语句或者finally语句，但是两者不能同时使用。else语句也不能与finally语句同时使用
python面向对象
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重载：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重载。
实例变量：定义在方法中的变量，只作用于当前实例的类。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
类和对象是面向对象编程的两个主要方面。类创建一个新类型，而对象是这个类的实例
包括初始化方法__init__,可以理解为构造，self，理解为this
Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找
实例的创建---通过调用类对象
1.定义类---Dog   类的方法其实指的就是函数，与普通函数的区别是，第一个参数必须是self
2.创建一个实例---dog
3.通过实例使用属性或方法--dog.greet()
对象初始化方法 __init__()
1.当类被调用后，python将创建实例对象
2.创建完对象后，python自动调用的第一个方法是__init__()
3.实例对象作为方法的第一个参数(self)被传递进去，调用类创建实例对象时的参数都传给__init__()
类属性
1.类的数据属性(静态成员) 仅仅是所定义的类的变量
2.在类创建后被使用
3.可以由类中的方法来更新，也可以在主程序中更新
4.类属于和实例无关，修改属性需要使用类名
继承
父类(基类)--字类(派生类)
def class parent():
        pass
def class son(parent)
        psss
方法的重载就是在子类中重新定义父类中的方法
默认情况下，python类的成员属性与方法都是"public"
双下划线(__) 防止父类和子类中的同名冲突
单下划线(_) 在属性名前使用一个单下划线，防止模块的属性用
python正则表达式
python 正则表达式使用re模块
re.compile(r'xxxx')    //先生成匹配规则
re.match函数 尝试从字符串的开始匹配一个模式
re.match(pattern,string,flags=0)
pattern 匹配的正则表达
string 要匹配的字符串
flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
匹配成re.match 方法返回一个匹配的对象，否则返回none
group(num=0)
groups()
re.match 尝试从字符串的开始匹配一个模式
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
re模块提供了re.sub用于替换字符串中的匹配项
re.sub(pattern, repl, string, max=0)
返回的字符串是在字符串中用 RE 最左边不重复的匹配来替换。如果模式没有发现，字符将被没有改变地返回。
可选参数 count 是模式匹配后替换的最大次数；count 必须是非负整数。缺省值是 0 表示替换所有的匹配。
正则表达式修饰符 - 可选标志
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
特殊字符类
实例	描述
.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'
* （星号） 指定前一个字符可以匹配0次或者多次，而不是只有1次，匹配结果会尽可能的重复多次最大不超过20亿次。（后面若加问号？变为非贪婪模式仅匹配0次：ab*? 结果为a）
+ （加号）   匹配前一个字符1次或者多次。（后面若加问号？变为非贪婪模式仅匹配1次：ab+? 结果为ab）
？ （问号） 匹配前一个字符0次或者1次。（后面若加问号？变为非贪婪模式仅匹配0次：ab?? 结果为a） ？可以是python原本的贪婪模式变为非贪婪模式   
{m} （花括号） m是数字，表示重复前一个字符m次。
{m,n} 表示重复前一个字符m-n次。若省略m则表示0-n次，若省略n表示m到无限次。（后面若加问号？变为非贪婪模式仅匹配0次：ab{2,100}? 结果为abb
字符串的起始和结尾 ^ $
单词的边界  \b  eg:\bThe\b
\A 匹配字符串的开始，\Z匹配字符串的结束
python 操作mysql
MySQLdb 是用于Python链接Mysql数据库的接口
import MySQLdb //引入模块
数据库查询操作
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall():接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
cursor用来执行命令的方法:
callproc(self, procname, args):用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
　    execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
　    executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
　    nextset(self):移动到下一个结果集
cursor用来接收返回值的方法：
fetchall(self):接收全部的返回结果行.
　    fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
　    fetchone(self):返回一条结果行.
　    scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一 行移动value条
try:
except:
print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：
print会依次打印每个字符串，遇到逗号“,”会输出一个空格
当我们写：a = 'ABC'时，Python解释器干了两件事情：
1. 在内存中创建了一个'ABC'的字符串；
2. 在内存中创建了一个名为a的变量，并把它指向'ABC'
使用\可对特殊字符进行转义
raw字符串与多行字符串
如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了
但是r'...'表示法不能表示多行字符串，也不能表示包含'和 "的字符串
如果要表示多行字符串，可以用'''...'''表示
还可以在多行字符串前面添加 r ，把这个多行字符串也变成一个raw字符串
最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），0 - 255被用来表示大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母 A 的编码是65，小写字母 z 的编码是122
Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
Unicode通常用两个字节表示一个字符，原有的英文编码从单字节变成双字节，只需要把高字节全部填为0就可以
因为Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码，普通的字符串'ABC'在Python内部都是ASCII编码的
Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示
如果中文字符串在Python环境下遇到 UnicodeDecodeError，这是因为.py文件保存的格式有问题。可以在第一行添加注释
# -*- coding: utf-8 -*-
目的是告诉Python解释器，用UTF-8编码读取源代码
如果我们要计算 11 / 4 的精确结果，按照“整数和浮点数混合运算的结果是浮点数”的法则，把两个数中的一个变成浮点数再运算就没问题了
因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
由于Python是动态语言，所以list中包含的元素并不要求都必须是同一种数据类型，我们完全可以在list中包含各种数据：
>>> L = ['Michael', 100, True]
一个元素也没有的list，就是空list：
>>> empty_list = []
通过索引来获取list中的指定元素
需要特别注意的是，索引从 0 开始，也就是说，第一个元素的索引是0，第二个元素的索引是1，以此类推L[0]
倒叙取数索引从-1开始，L[-1]倒数第一个
添加新元素 L.append('tom') 添加的元素位于列表的末尾
L.insert(0, 'Paul') 的意思是，'Paul'将被添加到索引为 0 的位置上（也就是第一个），而原来索引为 0 的Adam同学，以及后面的所有同学，都自动向后移动一位
删除列表中的元素
pop()方法总是删掉list的最后一个元素，并且它还返回这个元素，所以我们执行 L.pop() 后，会打印出 'Paul'
由于Paul的索引是2，因此，用 pop(2)把Paul删掉
对list中的某一个索引赋值，就可以直接用新的元素替换掉原来的元素，list包含的元素个数保持不变
tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了
创建tuple和创建list唯一不同之处是用( )替代了[ ]
获取 tuple 元素的方式和 list 是一模一样的，我们可以正常使用 t[0]，t[-1]等索引方式访问元素，但是不能赋值成别的元素
包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示：t()
正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,” t(1,)
tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a','b',['A','B']) 
Python代码的缩进规则。具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。
注意: if 语句后接表达式，然后用:表示代码块开始
利用 if ... else ... 语句，我们可以根据条件表达式的值为 True 或者 False ，分别执行 if 代码块或者 else 代码块。
注意: else 后面有个“:”。
if--elif--else
elif 意思就是 else if。这样一来，我们就写出了结构非常清晰的一系列条件判断。
特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。
利用for循环遍历list
L = ['a','b','c']
for name in L
    print name
我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
由于dict也是集合，len() 函数可以计算任意集合的大小：
>>> len(d)
3
注意: 一个 key-value 算一个，因此，dict大小为3。
可以简单地使用 d[key] 的形式来查找对应的 value，这和 list 很像，不同之处是，list 必须使用索引返回对应的元素，而dict使用key：
通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError
要避免 KeyError 发生，有两个办法：
一是先判断一下 key 是否存在，用 in 操作符：
if 'Paul' in d:
    print d['Paul']
如果 'Paul' 不存在，if语句判断为False，自然不会执行 print d['Paul'] ，从而避免了错误。
二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
>>> print d.get('Bart')
59
>>> print d.get('Paul')
None
dict的特点：
dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
由于dict是按 key 查找，所以，在一个dict中，key不能重复。
dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
dict的第三个特点是作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key
更新dict
d['test'] = 100 //在d中增加一个key=test，value=100的元素，如果key已经存在就覆盖原来的值
遍历dict
直接使用dict的key实现遍历
for key in d:
    print key + ':', d[key]
dict的作用是建立一组 key 和一组 value 的映射关系，dict的key是不能重复的。
有的时候，我们只想要 dict 的 key，不关心 key 对应的 value，目的就是保证这个集合的元素不会重复，这时，set就派上用场了。
set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。 
创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
>>> s = set(['A', 'B', 'C'])
set内部存储的元素是无序的,set会自动去掉重复的元素
由于set存储的是无序集合，所以我们没法通过索引来访问。
访问 set中的某个元素实际上就是判断一个元素是否在set中,用 in 操作符判断
s = set(['a','b'])
'a' in s //判断元素是否在s 中，在返回true，不在返回false
set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
最后，set存储的元素也是没有顺序的。
set 遍历
由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现
更新set
由于set存储的是一组不重复的无序元素，因此，更新set主要做两件事：
一是把新的元素添加到set中，二是把已有元素从set中删除。
s = set([1,2,3])
s.add(4)    //如果重复不会报错，同时添加不进去
s.remove(1)    //从set中删除元素,如果不存在则引发 keyError
s.discard() 如果在s 中存在元素x，则删除
s.pop() 删除并返回一个不确定的元素，如果为空引发keyerror
s.clear() 删除 s 中的所有元素
python中内置函数
abs() // 求绝对值
cmp(x,y)    //比较函数
int()
str()
sum()    //接受一个list作为参数，并返回list所有元素之和
在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回
函数返回多个值 return nx, ny
在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
def fn(*args):
    print args
可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
对list进行分片，方便获取list中的元素
L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
如果第一个索引是0，还可以省略L[:3]，只用一个 : ，表示从头到尾：
切片操作还可以指定第三个参数：
>>> L[::2]
['Adam', 'Bart']
第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个
把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple
>>> range(1,10)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
倒叙切片
对于list，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引
>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L[-2:]
['Bart', 'Paul']
>>> L[:-2]
['Adam', 'Lisa']
>>> L[-3:-1]
['Lisa', 'Bart']
>>> L[-4:-1:2]
['Adam', 'Bart']
对字符串切片
>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[-3:]
'EFG'
>>> 'ABCDEFG'[::2]
'ACEG'
字符串有个方法 upper() 可以把字符变成大写字母：
>>> 'abc'.upper()
'ABC'
在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）
因为 Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。
因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
注意: 集合是指包含一组元素的数据结构，我们已经介绍的包括：
1. 有序集合：list，tuple，str和unicode；
2. 无序集合：set
3. 无序集合并且具有 key-value 对：dict
索引迭代
Python中，迭代永远是取出元素本身，而非元素的索引
对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？
方法是使用 enumerate() 函数
索引迭代也不是真的按索引访问，而是由 enumerate() 函数自动把每个元素变成 (index, element) 这样的tuple，再迭代，就同时获得了索引和元素本身。
dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value
dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v
# 85
# 95
# 59
那这两个方法有何不同之处呢？
1. values() 方法实际上把一个 dict 转换成了包含 value 的list。
2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
迭代dict的key和value
我们了解了如何迭代 dict 的key和value，那么，在一个 for 循环中，能否同时迭代 key和value？答案是肯定的。
首先，我们看看 dict 对象的 items() 方法返回的值：
>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> print d.items()
[('Lisa', 85), ('Adam', 95), ('Bart', 59)]
可以看到，items() 方法把dict对象转换成了包含tuple的list，我们对这个list进行迭代，可以同时获得key和value：
>>> for key, value in d.items():
...     print key, ':', value
...
Lisa : 85
Adam : 95
Bart : 59
和 values() 有一个 itervalues() 类似， items() 也有一个对应的 iteritems()，iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() 不占用额外的内存
[x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
这种写法就是Python特有的列表生成式。利用列表生成式，可以以非常简洁的代码生成 list。
写列表生成式时，把要生成的元素 x * x 放到前面，后面跟 for 循环，就可以把list创建出来
复杂表达式
使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。
假设有如下的dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格：
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串
 join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
a-b-c

列表生成式的 for 循环后面还可以加上 if 判断
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。
isinstance(x, str) 可以判断变量 x 是否是字符串；
字符串的 upper() 方法可以返回大写的字母。
多层表达式
for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表
对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
>>> [m + n for m in 'ABC' for n in '123']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
print [100 * n1 + 10 * n2 + n3 for n1 in range(1, 10) for n2 in range(10) for n3 in range(10) if n1==n3]
python中try except处理程序异常的三种常用方法
1.捕获所有异常
try:  
    a=b  
    b=c  
except Exception,e:  
    print Exception,":",e
2.采用traceback模块
#引入python中的traceback模块，跟踪错误
import traceback  
try:  
    a=b  
    b=c  
except:  
    traceback.print_exc()
3.采用sys模块回溯最后的异常
#引入sys模块
import sys  
try:  
    a=b  
    b=c  
except:  
    info=sys.exc_info()  
    print info[0],":",info[1]
如果你还想把这些异常保存到一个日志文件中，来分析这些异常，那么请看下面的方法：
把　traceback.print_exc()　打印在屏幕上的信息保存到一个文本文件中
import traceback
try:  
    a=b  
    b=c  
except:  
    f=open("c:log.txt",'a')  
    traceback.print_exc(file=f)  
    f.flush()  
    f.close()
Python使用SMTP发送邮件
python的smtplib提供了一种很方便的途径发送电子邮件
import smtplib
smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
第三个参数，msg是字符串，表示邮件
>>> import smtplib
>>> dir(smtplib)    //查看模块的函数和方法
python 中__name__ = '__main__' 的作用，到底干嘛的？
有句话经典的概括了这段代码的意义：
“Make a script both importable and executable”
意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行。
如果我们是直接执行某个.py文件的时候，该文件中那么”__name__ == '__main__'“是True,但是我们如果从另外一个.py文件通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main__
Python 操作mysql
connection   连接数据库
cursor 与数据库进行交互
exception 数据库异常类
python访问数据库的流程
开始----connection----cursor---执行数据库的操作---关闭cursor/connection
connection支持的方法
1.cursor()   使用该连接创建并返回游标
2.commit()    提交当前事务
3.roolback()    回滚当前事务
4.close()    关闭连接
游标对象用于执行查询和获取结果
execute()    执行一个数据库的查询和命令
fetchone()    取的结果集的下一行数据
fetchmany(size)    取的结果集的下N行数据
fetchall()    取得结果集中剩下的所有行
rowcount    最近一次execute影响的行数
close() 关闭
#写入      
sql = "insert into user(name,created) values(%s,%s)"    
param = ("aaa",int(time.time()))      
n = cursor.execute(sql,param)      
print 'insert',n 
#执行,如果成功,n的值为1 
#写入多行      
sql = "insert into user(name,created) values(%s,%s)"    
param = (("bbb",int(time.time())), ("ccc",33), ("ddd",44) )  
n = cursor.executemany(sql,param)      
print 'insertmany',n 
#更新      
sql = "update user set name=%s where name='aaa'"    
param = ("zzz")      
n = cursor.execute(sql,param) 
#查询      
n = cursor.execute("select * from user")      
for row in cursor.fetchall():      
    print row  
    for r in row:      
        print r  
sql = "delete from user where name=%s"    
param =("bbb")      
n = cursor.execute(sql,param)      
print 'delete',n  

cursor.close()      
#提交      
conn.commit()  
#关闭      
conn.close()
编码（防止乱码）
#encoding=utf-8  
import sys  
import MySQLdb     
reload(sys)  
sys.setdefaultencoding('utf-8')  
db=MySQLdb.connect(user='root',charset='utf8') 
python中的异常
Exception类是常用的异常类，该类包括StandardError，StopIteration, GeneratorExit, Warning等异常类。
StandardError类是python中的错误异常，如果程序上出现逻辑错误， 将引发该异常。StandardError类是所有内敛异常的基类，放置在默认的命名空间中，因此使用IOEroor,
EOFError, ImportError等类，不需要导入exception模块。
StopIteration类判断循环是否执行到尾部，如果循环到尾部，则抛出该异常。
GeneratorExit类是由Generator函数引发的异常，当调用close（）时引发该异常。
Warning类表示程序中的代码引起的警告。
python中的异常使用继承结构创建，可以在异常处理程序中捕获基类异常，也可以捕获各种子类异常，python中使用try...except语句捕获异常，异常子句定义在try子句后面。
try...except的使用方法
try...except用于处理问题语句，捕获可能出现的异常。try子句中的代码块放置可能出现异常的语句，except子句中的代码块处理异常。
try...finally的使用方法
try...except后还可以添加一个finally子句。无论异常是否发生，finally子句都会被执行。所有的finally子句通常用于关闭因异常而不能释放的系统资源
使用raise抛出异常
当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。
自定义异常
python允许程序员自定义异常，用于描述python中没有涉及的异常情况，自定义异常必须继承Exception类，自定义异常按照命名规范以"Error"结尾，显示地告诉程序员这是异常。自定义异常使用raise语句引发，而且只能通过人工方式触发。
assert语句的使用
assert语句用于检测某个条件表达式是否为真。assert语句又称为断言语句，即assert认为检测的表达式永远为真，if语句中的条件判断都可以使用assert语句检测
python sys模块
1.sys.argv 外部传参
Import sys
Print sys.argv[number]
一般情况下，number为0是这个脚本的名字，1，2…则为命令行下传递的参数
2.sys.platform
3.sys.exit(n)
执行至主程序的末尾时,解释器会自动退出. 但是如果需要中途退出程序, 你可以调用sys.exit 函数, 它带有一个可选的整数参数返回给调用它的程序. 这意味着你可以在主程序中捕获对sys.exit 的调用。（注：0是正常退出，其他为不正常，可抛异常事件供捕获!）
4.sys.path 模块的路径 sys.path.append('xxxx')
5.Python程序的标准输入/输出/出错流定义在sys模块中，分别 为： sys.stdin,sys.stdout, sys.stderr
Python中使用线程有两种方式：函数或者用类来包装线程对象
函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:
thread.start_new_thread ( function, args[, kwargs] )
参数说明:
    function - 线程函数。
    args - 传递给线程函数的参数,他必须是个tuple类型。
    kwargs - 可选参数。
线程的结束一般依靠线程函数的自然结束；也可以在线程函数中调用thread.exit()，他抛出SystemExit exception，达到退出线程的目的
类和对象
类是对象的抽象，而对象是类的具体实例。类是抽象的，不占用内存，而对象是具体的，占用存储空间。类是用于创建对象的蓝图，它是一个定义包括在特定类型的对象中的方法和变量的软件模板
 类类型的声明
class 类名
{
public：
公用的数据和成员函数
protected：
保护的数据和成员函数
private：
私有的数据和成员函数
};
re模块
正则表达式使用的模块
\A 和\Z    指定的字符串匹配必须出现在开头/结尾
^ $ 开头和结尾
(?P<name>) 给分组起别名
(?P=name) 引用别名为name的分组
re.match()    只能匹配开头的，同时只能查询出一个匹配的值
re.search(pattern,string,flags=0)    查找首次出现的，同时只能查询出一个匹配的值
findall(patten,string,flags=0)    找到匹配，返回所有匹配部分的列表，能够查询出所有匹配的值，是一个列表的数据类型
>>> strl = 'imooc videonum 100000'
>>> test = re.search('\d+',strl)
>>> test.group()                  
'100000'
sub(pattern,repl,string,count=0,flags=0)替换    repl可以是一个函数，传入函数中的值是正则比配的内容
split(pattern,string,maxsplit=0,flags=0)切割
python错误异常
python常见的错误类型
1.NameError
2.if True:syntaxError
3.f = open('1.txt'):IOError
4.10/0 ZeroDivisionError
5.a =int('ddd') ValueError
try-except 异常处理
try:
    try_suite
except Exception,e:
    exception_block
1.try用来捕获try_suite中的错误，并且将错误交给except处理
2.except用来处理异常，如果处理异常和设置捕获异常一致，使用exception_block处理异常
try-finally语句
try:
    try_suite
finally:
    do_finally
1.如果try没有捕获错误，代码执行do_finally语句
2.如果try语句捕获错误，程序首先执行do_finally语句，然后将捕获到的错误交给python解释器处理
规则:try-finally无论是否检测到异常，都会执行finally代码
finally的作用是为异常处理提供清理机制，用来关闭文件或者释放系统资源
try-except-finally使用:
没异常:try---finally
有异常:except---finally
try-except-else-finally:
没异常:try--else--finally
有异常:except--finally
with语句
with context [ as var]:
    with_suite
1.with语句用来代替try-except-finally语句
2.context 表达式返回是一个对象
3.var 用来保存context返回对象，单个返回值或元组
4.with_suite 使用var变量来对context放回对象进行操作
raise 语句用于主动抛出异常
assert语句用于检测表达式是否为真，如果为假，引发assertionerror错误
python文件处理
文件的打开 open(name[,mode[buf]])
name 文件的路径
mode 打开文件的模式
r 只读方式 文件必须存在
w 只写方式    文件不存在创建，存在则清空文件内容
a 追加方式打开 文件不存在创建文件
r+/w+ 读写方式打开
a+追加和读写方式打开
二进制方式打开，都加b即可，eg:ab+;aw+
buf缓存大小
读取方式 
read([size]) 读取size个字节，默认读取全部
readline([size]) 读取一行
readlines([size]) 读取完文件，返回每一行所组成的列表,会把文件读入到缓存中，默认缓存是8019字节
iter 使用迭代器读取文件
文件的写入
write(str) 将字符串写入文件
writelines(sequence_of_strings) 写多行到文件
文件读取写入文件指针移动过程:
文件指针操作
seek(offset,whence) 移动文件指针
offset 偏移量，可以为负数
whence 偏移相对位置
文件指针定位方式
os.SEEK_SET :相对起始位置
os.SEEK_CUR 相对文件当前位置
os.SEEK_END 相对文件结尾位置
python文件属性
file.fileno()    文件描述符
file.mode 文件打开权限
file.encoding 文件编码格式
file.closed 文件是否关闭
python标准文件
文件标准输入:sys.stdin
文件标准输出:sys.stdout
文件标准错误:sys.stderr
使用raw_input() 调用的是sys模块中的sys.stdin
使用print 打印文件，调用的是sys模块中的sys.stdout
python文件命令行参数
sys模块提供sys.argv 属性，通过该属性可以得到命令行参数
sys.argv 字符串组成的列表
文件编码格式
a = unicode.encode(u'慕课','utf-8')
使用codecs 模块提供方法创建指定编码格式文件
open(fname,mode,encoding,errors,buffering)
使用指定编码格式打开文件
使用os模块打开文件
os.open(filename,flag[,mode]) 打开文件 返回是文件的描述符
flag:打开文件方式
os.O_CREAT 创建文件
os.O_RDONLY 只读方式打开
os.O_WRONLY 只写方式打开
os.O_RDRW 读写方式打开
os.read(fd,buffersize) 读取文件
os.write(fd,string)    写入文件
os.lseek(fd,pos,how) 文件指针操作
os.close(fd) 关闭文件
os模块方法简介
os方法
access(path,mode)    判断文件权限:F_OK ;R_OK;W_OK,X_OK  os.access('dong.txt',os.F_OK)
listdir(path) 返回当前目录下所有文件组成的列表
remove(path) 删除文件
rename(old,new) 修改文件或目录名
mkdir(path[,mode]) 创建目录
mkdirs(path[,mode]) 创建多级目录
removedirs(path) 删除多级目录
rmdir(path) 删除目录,目录必须为空
os.path方法
exits(path) 判断当前路径是否存在
isdir(s) 是否是一个目录
isfile(path) 是否是一个文件
getsize(filename) 返回文件大小
dirname(p) 返回路径的目录
basename(p) 返回路径的文件名
python 爬虫
简单爬虫的架构
1.URL管理器    管理将于访问的url和已经访问的url
2.网页下载器    把访问的url的内容下载下来
3.网页解析器    对下载下来的URL进行解析，获取需要的数据
正则表达式  html.parser beautifulsoup lxml 
结构化解析-DOM (document object model)树
网页解析器beautifulsoup语法
beautifulsoup4 模板的安装pip install beautifulsoup4 
html网页---创建beautifulsoup对象---find_all,find----访问节点的名称、属性等
Django
安装pip install ipython
pip install Django
django-admin startproject mysite    //配置项目
python manger.py runserver     //    启动网站
python2.7.3 django 1.8
python2.6 升级到2.7
1.下载2.7的源码
./configure
make all
make install
make clean
make distclean
2.建立软连接
mv /usr/bin/python /usr/bin/python2.6.6
ln -s /usr/local/bin/python2.7 /usr/bin/python
3.修改vim /usr/bin/yum 
#/usr/bin/python2.6
升级pip 和setuptool
1.setuptool
wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg  --no-check-certificate 
      #chmod +x setuptools-0.6c11-py2.7.egg
      #sh setuptools-0.6c11-py2.7.egg
2.pip
wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz
tar zvxf 1.5.5.tar.gz    #解压文件
cd pip-1.5.5/
python setup.py install
mv /usr/bin/pip /usr/bin/pip2.6.6
ln -s /usr/local/bin/pip /usr/bin/pip     //把新版的pip进行软连接
3.安装sqlite3
python2.7 django1.8 bootstrap 三者开发web网站
遇到的问题:
1. python2.6.6 升级到2.7后，引入sqlite3 出错
    _sqlite3.so 把2.6.6目录下的_sqlite.so复制到2.7对应目录下即可
2.UnicodeDecodeError: ‘ascii’ codec can’t decode byte 0xe5 in position 108: ordinal not in range(128
    修改mimetypes.py文件，路径位于python的安装路径下的Lib\mimetypes.py文件。在import下添加如下几行：
    if sys.getdefaultencoding() != 'utf8':
     reload(sys)
     sys.setdefaultencoding('utf8')
django-admin startproject HelloWorld //创建一个www项目
HelloWorld: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
HelloWorld/settings.py: 该 Django 项目的设置/配置。
HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
python manage.py runserver 0.0.0.0:8000
0.0.0.0让其它电脑可连接到开发服务器，8000为端口号。如果不说明，那么端口号默认为8000
视图和 URL 配置
在先前创建的 HelloWorld 目录下的 HelloWorld 目录新建一个 view.py 文件，并输入代码：
from django.http import HttpResponse
def hello(request):
 return HttpResponse("Hello world ! ")
接着，绑定 URL 与视图函数。打开 urls.py 文件，删除原来代码，将以下代码复制粘贴到 urls.py 文件中：
from django.conf.urls import *
from HelloWorld.view import hello
urlpatterns = patterns("",
 ('^hello/$', hello),
)
 urls.py              # url 配置
view.py              # 添加的视图文件
得到当前工作目录，即当前Python脚本工作的目录路径：os.getcwd()
返回指定目录下的所有文件和目录名：os.listdir()
函数用来删除一个文件：os.remove()
删除多个目录：os.removedirs(r"c:\python")  //略危险，熟练之后再用吧
检验给出的路径是否是一个文件：os.path.isfile()   //经常会用
检验给出的路径是否是一个目录：os.path.isdir()    //经常会用
判断是否是绝对路径：os.path.isabs()
检验给出的路径是否真实存在：os.path.exists()
返回一个路径的目录名和文件名：os.path.split()
例：import os
os.path.split('/home/swaroop/byte/code/poem.txt')
结果为：('/home/swaroop/byte/code','poem.txt')     //就是把路径和文件名分别列出来显得更加清楚
分离扩展名：os.path.splitext()
获取路径名：os.path.dirname()
获取文件名：os.path.basename()
运行shell命令：os.system()
读取和设置环境变量：os.getenv()与os.putenv()
给出当前平台使用的行终止符：os.linesep   windows使用'\r\n',linux使
用'\n'而mountainlion使用的是'\r'
显示你正在使用的平台：os.name 对于windows，他是'nt'，而对于linux/unix
，他是'posix'
重命名：os.rename(old,new);
创建多集目录：os.makedirs(r"c:\python\test")
创建单个目录：os.mkdir("test")
获取文件属性 os.stat(file)
修改文件权限和时间戳：os.chmod(file)
终止当前进程：os.exit()  //python2.4可用
获取文件大小：os.path.getsize(filename)
文件操作：
os.mknod("test.txt")    创建空文件
fp = open("test.txt",w) 直接打开一个文件，如果文件不存在则创建文件
关于open/file的模式：
w 以写的方式打开
a 以追加的模式打开（从EOF开始，必要时创建新文件）
r+ 以读写模式打开
w+ 以读写模式打开 //据说不好用
a+ 以读写模式打开 //我比较喜欢用，读写打开后追加
rb 以二进制读模式打开
wb 以二进制写模式打开
ab 以二进制追加模式打开
rb+ 以二进制读写模式打开
wb+ 以二进制读写模式打开
ab+ 以二进制读写模式打开
fp.read([size])     //size 为读取长度，以byte为单位
fp.readline([size]) //读一行，如果定义了size，有可能返回的只是一行的一
部分
fp.write(str)    //把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq) //把seq的内容全部写到文件中（多行一次性写入）。这个
函数也只是忠实地写入，不会在每行后面加任何东西
fp.close()  
fp.flush()      //把缓冲区的内容写入硬盘
fp.fileno()     //返回一个长整形的“文件标签”
fp.isatty() //文件是否是一个终端设备文件（unix系统中的）
fp.tell() //返回当前位置，比如：
fp = open("zhige.txt",'a+')  //zhige.txt里的内容为zhigedahaoren
fp.read(3)
c = fp.tell()
print c   //会返回显示zhigedahaoren里的第三个字母i
fp.next()   //返回下一行，并将文件操作标记位移动到下一行
把一个file用于for...in file 这样的语句时，就是调用next()函数来实现遍历
的
fp.seek(offset[,whence])   //讲文件的游标移动到offset的位置和tell搭配
做实验看比较明显
fp.truncate([size])    //把文件裁成规定的大小，默认的是裁到当前文件操
作坐标的位置。如果size比文件大小还要大，依据系统的不同，可能是不改变文
件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。
目录操作：   //感觉可以用 os.system('')里写shell完成
os.mkdir("file")  创建目录
复制文件：
shutil.copyfile("oldfile","newfile")  //oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile") //oldfile只能是文件，newfile可
以是文件，也可以是目标目录
复制文件夹：
shutil.copytree("olddir","newdir") //olddir和newdir都只能是目录，
且newdir必须不存在
重命名文件（目录）：
os.rename("oldname","newname") //文件或目录都是这条命令
移动文件（目录）
shutil.move("oldpos","newpos")
删除文件
os.remove("file")
删除目录：
os.rmdir("dir")  //只能删除空目录
shutil.rmtree("dir") //空目录，有内容的目录都可以删
转换目录：
os.chdir("path")   //更换路径
一些详解：
seek(offset,where): where=0从起始位置移动，1从当前位置移动，2
从结束位置移动。当有换行时，会被换行截断。seek()无返回值，故值为None。
tell(): 文件的当前位置，即tell是获得文件指针的位置，受
seek,readline,read,readlines影响，不受truncate影响
truncate(n)：从文件的首行字符开始截断，截断文件为n个字符；无n
表示从当前位置起截断；阶段之后n后面的说有字数被删除。其中win下的换行代
表2个字符大小。
readline(n)：读入若干行，n表示读入的最长字节数。其中读取的开始
位置为tell()+1。当n为空时，默认只读当前行的内容
readlines 读入所有行内容
read 读入所有行内容
二、以下以一个例子说明以上各函数的作用
fso = open("f:\\a.txt"，'w+')    //以w+方式，并非a方式打开文件，故文件
原内容被清空
print fso.tell()   //文件原内容被清空，故此时tell()=0
fso.write("abcde\n") //写入文件abcde\n，因为换行\n占2个字符，故写入了7
个字符
print fso.tell()  此时tell()=7
fso.write("fghwm") //又写入文件fghwm，故此时文件共写入7+5=12个字符
print fso.tell()   //此时tell()=12
fso.seek(1,0)  //从其实位置即文件首行首字符开始移动一个字符
print fso.tell()   //此时tell()=1
print fso.readline() //读取当前行，即文件的第一行，但是会从第二个字符
开始读，结果为bcde
//若换成for读取整个文件或者read读取整个文件则结果为bcdefghwm
print fso.tell()   //因为readline此时tell()=7
fso.truncate(8) //从写入后文件的首行字符开始算，截断为8个字符，即
abced\nf，即文件内容为：abcde\nf
print fso.tell()  //tell()依旧为7，并为受truncate(8)的影响，但此时文件
的内容为abcde\nf
print fso.readline()  //从tell()+1=8 开始读取，读取当前行内容：f
map()函数不改变原有的 list，而是返回一个新的 list。
利用map()函数，可以把一个 list 转换为另一个 list，只需要传入转换函数。
def f(x):
    return x*x
print map(f,[1,2,3,4])
reduce()函数也是Python内置的一个高阶函数。reduce()函数接收的参数和 map()类似，一个函数 f，一个list，但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
def f(x,y):
    return x+y
reduce(f,[1,2,3])    //得出的结果是累加和
reduce()还可以接收第3个可选参数，作为计算的初始值
filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
 s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')，如下：
a = '     123'
a.strip()
结果： '123'
Python内置的 sorted()函数可对list进行排序：
>>>sorted([36, 5, 12, 9, 21])
[5, 9, 12, 21, 36
Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！
返回的函数是函数的名字 g ，g()调用函数
像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变
匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
 map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
关键字lambda 表示匿名函数，冒号前面的 x 表示函数参数。
装饰函数
Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码
要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw
偏函数
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
模块的引用
#test.py    自身模块名
import math    引用math模块
print math.pow(3,4)    调用match模块的函数
同名的模块放入不同的包中
文件系统中包就是文件夹，模块就是文件名
如何区分包和普通目录，包下面必须有个__init__.py文件，每层包下面都必须有
模块的引入
import 模块名
from math import pow, sin, log //仅引入模块的某几个函数
from logging import log as logger   # logging的log现在变成了logger
当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到__future__中，以便旧的代码能在旧版本中测试新特性
面向对象编程的基本思想
类和实例
类用于定义抽象类型
实例是根据类的定义被创建出来的
类的定义 class person:
实例 小明 = person()
在Python中，类通过 class 关键字定义
按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的
有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用 类名+()
**kw **xarg //接收任意参数
初始化实例属性
虽然我们可以自由地给一个实例绑定各种属性，但是，现实世界中，一种类型的实例应该拥有相同名字的属性，
在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
__init__() 方法的第一个参数必须是 self（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别。
Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问
可见，只有以双下划线开头的"__job"不能直接被外部访问。
但是，如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义。
以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。
类是模板，而实例则是根据类创建的对象。
绑定在一个实例上的属性不会影响其他实例，但是，类本身也是一个对象，如果在类上绑定一个属性，则所有实例都可以访问类的属性，并且，所有实例访问的类属性都是同一个！也就是说，实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。
可见，当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性
一个实例的私有属性就是以__开头的属性，无法被外部访问
实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：
在实例方法内部，可以访问所有实例属性，这样如果外部需要访问私有属性，可以通过方法调用获得
在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象
因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数变为一个方法
types.MethodType()可以把一个函数变为一个方法
import types
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
types.MothodType(函数名,实例名,类名)
和属性类似，方法也分实例方法和类方法
在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身
通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。类方法的第一个参数将传入类本身，通常将参数名命名为 cls
因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用
类的继承
新类不必从头编写
新类从现有的继承，就拥有了现有类的所有功能
新类只需要编写现有类缺少的新功能
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
一定要用 super(Student, self).__init__(name, gender) 去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。
函数super(Student, self)将返回当前类继承的父类，即 Person ，然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，不需要写出（也不能写）
函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，也可以用在我们自定义的类，它们本质上都是数据类型
这是动态语言和静态语言（例如Java）最大的差别之一。动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。
除了从一个父类继承外，Python允许从多个父类继承，称为多重继承
多重继承的目的是从两种继承树中分别选择并继承出子类，以便组合功能使用。
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass
class D(A,C)
type() 函数获取变量的类型
dir() 函数获取变量的所有属性
dir()返回的属性是字符串列表，如果已知一个属性名称，要获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数了
setattr(s, 'name', 'Adam')  # 设置新的name属性
传入**kw 即可传入任意数量的参数，并通过 setattr() 绑定属性
**kw是关键字参数，用于字典
iteritems()用于字典kw的遍历
setattr(self, k, v)就等价于self.k = v
综上就是，遍历dict kw 中的属性，给每个属性设置了属性值
Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员
__str__()用于显示给用户，>>> print p
而__repr__()用于显示给开发人员。>>> p
对 int、str 等内置数据类型排序时，Python的 sorted() 按照默认的比较函数 cmp 排序，但是，如果对一组 Student 类的实例排序时，就必须提供我们自己的特殊方法 __cmp__()
如果一个类表现得像一个list，要获取有多少个元素，就得用 len() 函数。
要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数
1.python中的self是指对象本身，本题中类方法中的self与r分别指两个对象r1,r2；
2.python规定，类中第一个参数必须是self。其次运算符是Rational类中绑定的，
3.用 + 表示调用类的__add__()方法
4.同理 减法运算：__sub__
乘法运算：__mul__
除法运算：__div__
Rational类实现了有理数运算
要让int()函数正常工作，只需要实现特殊方法__int__():
顾名思义，__slots__是指一个类允许的属性列表：
__slots__的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存
一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
subprocess 模块执行linux命令
subprocess.call(["ls","-l"])
subprocess.call("ls -l",shell=True)
python作为一种脚本语言，我们用python写的各个module都可以包含以上那么一个类似c中的main函数，只不过python中的这种__main__与c中有一些区别，主要体现在：
1.当单独执行时，可以理解为"if __name__=="__main__":" 这一句与c中的main()函数所表述的是一致的，即作为入口；
2.当该module被其它module 引入使用时，其中的"if __name__=="__main__":"所表示的Block不会被执行,这是因为此时module被其它module引用时，其__name__的 值将发生变化，__name__的值将会是module的名字
ipython提供了一个__IP,__IP实际上是一个交互式shell对象，拥有一个叫做alias_table的属性
ipython 模式下mglog rec:*.py 查询后缀为py的文件
pinfo subprocess //查看模块的基本信息
psource subprocess //查看模块的源码
psearch 不但能够一句名称查找python对象，还可以使用通配符协助查找
psearch 默认搜索builtin user空间，可以使用 -e选项排除搜索
who whos who_ls
在字符前用r，可以创建一个元素的字符r'\n'
in not in  //可以判断一个字符串是否是另一个字符的子集
find    index    //可以确定子字符串出现的具体位置，二者的区别index对不存在的字符查询抛出错误，find返回-1
string[index:]    //从查找的字符的位置开始到末尾
startswith()    endswith()    //判断字符是否以XX开头或结尾
lstrip()    删除开始出的空白
rstrip()    删除结尾处的空白
strip()    删除字符串开头和结尾处的空白  //空白指tab 空格 回车 换行
strip('xxx')    //可以删除指定的字符    lstrip('xx')    //只删除开头的指定字符    rstrip('xxx')    //只删除结尾的指定字符
upper() lower()  s='test'    s.upper()  //把字符串进行大小写转换
split()   默认以空格为分割符，把一串字符串进行分割，split(",")    把一串字符串以逗号为分隔符进行分割，得到的是列表['a','b']
split(',',1)    //以逗号为分割，但是仅对第一次出现的逗号定界符进行分割
splitlines()    //对多行进行分割，得到列表['x','xxx'],然后再利用循环对每行进行split()
join()  ','.join(some_list)  //将多个字符串连接起来，join()连接的是一个字符串序列，如果不是字符串需要转换下 join(str(i) for in list)
re_string.replace("aaa","bbb")    //把字符串中的aaa 替换为bbb ,分割操作以及strip() ,replace() 不会对原字符串进行操作，而是产生一个新的字符串
python中，“%”是一个特殊字符，需要两个“%%”才表示一个“%”
python传参
def get_data(table,number):
    sql="select * from %s where id=%s" %(table,number)
    ......
get_data(books,1001)
collections模块基本介绍
1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
主要用来产生可以使用名称来访问元素的数据对象，通常用来增强代码的可读性， 在访问一些tuple类型的数据时尤其好用。
Website = namedtuple('Website', ['name', 'url', 'founder'])
                                        元组名        对应名
2.deque: 双端队列，可以快速的从另外一侧追加计数器是一个非常常用的功能需求，collections也贴心的为你提供了这个功能。和推出对象
其实是 double-ended queue 的缩写，翻译过来就是双端队列，它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft() 
3.Counter: 计数器，主要用来计数
计数器是一个非常常用的功能需求，collections也贴心的为你提供了这个功能。
4.OrderedDict: 有序字典
ordered_dict = OrderedDict(items)
for k, v in ordered_dict.items():
    print k, v
5.defaultdict: 带有默认值的字典
在使用Python原生的数据结构dict的时候，如果用 d[key] 这样的方式访问， 当指定的key不存在时，是会抛出KeyError异常的。
但是，如果使用defaultdict，只要你传入一个默认的工厂方法，那么请求一个不存在的key时， 便会调用这个工厂方法使用其结果来作为这个key的默认值
#!/usr/bin/python

from collections import defaultdict

lists=('master','slave1')

a = ('master',20)
b = ('slave1',90.1)
c = ('master',21)
d = ('slave1',2)
e=[]
e.append(a)
e.append(b)
e.append(c)
e.append(d)

result = defaultdict(list)
for name,value in e:
        result[name].append(value)

for k in result:
        data = k,result[k][0],result[k][1]
        print data
re 模块
什么是已编译的正则表达式？它是一个简单的对象，通过传递一个模式给re.complie()来创建，它包括一些正则表达式方法，也通过传递
模式给re.complie()来创建，使用编译和非编译存在的主要区别是，使用模式来创建一个编译的正则表达式，没有在re模块中调用findall()
而是在编译后的表达式对象上调用findall()
re_string="{{(.*?)}}"
for match in re.findall(re_string,some_string):
已编译模式
re.obj =re.complie("{{(.*?)}}")
for match in re.obj.findall(som_string):
raw string就是用'r'作为字符串的前缀，如 r"\n"：表示两个字符"\"和"n"，而不是换行符了
match和search。match是从字符串的起点开始做匹配，而search（perl默认）是从字符串做任意匹配
re.compile()
prog = re.compile(pattern)
result = prog.match(string)
跟
result = re.match(pattern, string)
是等价的。
re.split(pattern, string, maxsplit=0)
通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数
it = re.finditer(r"\d+","12a32bc43jf3")
>>> for match in it:
              print match.group()
简单的说吧，就是finditer返回了一个可调用的对象，使用 for i in finditer()的形式，可以一个一个的得到匹配返回的 Match对象。这在对每次返回的对象进行比较复杂的操作时比较有用
re_obj.match(string，pos=1,endpos=3)    //指定开始和结束的位置
match()的方法 start()--返回一个整数，是模式开始匹配的起始位置  end()--结束位置 span()--开始和结束位置
groups()--返回匹配的多元组 groupdict()--返回一个字典类型的匹配数据
读取文件
read()    //会尽可能地读取文件的内容 read(5) 读取5个字符
readline()    //一次读取文件的一行，readline(size)在返回一个字符串对象之前读取的最大字节数，而无论是否达到行的结尾
readlines()    //读取文件的所有行，readlines(100)用于指定读入字符的大约总数
写文件
write()
writelines() 必须有一个参数，要写入打开文件的序列，该序列可以是列表，元组，任何迭代对象
例如:f.writelines("%s \n" % i for i in range(10))
需要注意的是writelines()无法写入一个新行(\n),你需要在写入的序列中使用"\n"
python清空list的方法
1.大数据量的list，要进行局部元素删除，尽量避免用del随机删除，非常影响性能，如果删除
量很大，不如直接新建list，然后用下面的方法释放清空旧list。
2.对于一般性数据量超大的list，快速清空释放内存，可直接用 a = [] 来释放。其中a为
list。
3.对于作为函数参数的list，用上面的方法是不行的，因为函数执行完后，list长度是不变
的，但是可以这样在函数中释放一个参数list所占内存： del a[:]，速度很快，也彻底
将一个字符串转换为文本使用StringIO
from StringIO import StringIO
file = StringIO("this is a test string")
reStructuredText 将纯文本文件转换成HTML文件，利用docutils.core 模块
利用textile 对纯文件文件转换成html文件
信息格式化利用
gdchart 进行绘图
python判断文件和文件夹是否存在、创建文件夹 
import os
os.path.exits('file')
os.path.isfile('file')
使用os.path.exists()方法可以直接判断文件是否存在
os.path.isdir('dirname')    //python判断文件夹是否存在
if __name__ =="__main__":
脚本中定义了这个的作用是，单独执行本脚本时，开始执行__name__这个命令下的代码，如果把本脚本文件通过文件名导入到其他
脚本，就不会执行__name__下面的代码
socekt编程
socekt 通信流程
TCP客户端：
socekt()--->connect()--->write()--->read()--->close()
TCP服务端:
socket()--->bind()--->listen()---accept()--->read()--->write()--->read()-->close()
客户端的connect连接，服务端accept进行接收；
客户端write把请求发过服务端，服务端利用read()进行读取请求的信息然后利用write进行处理发给客户端的read
处理完毕后，最后客户端close关闭连接，服务端read到一个关闭信号，然后也关闭本次连接
socket服务器端编程主要包括下面几步:
1.打开socket
2.绑定到一个地址和端口
3.侦听进来的连接
4.接收连接
5.读写数据
socket 类型： AF---地址簇
socket.AF_UNIX 只能够用于单一的unix系统进程间通信
socket.AF_INET 服务器之间网络通信
socket.AF_INET6 IPV6
socket.SOCK_STREAM 流式socket for tcp
socket.SOCK_DGRAM 数据报式socket for udp
socket.SOCK_RAW 原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以，其次sock_RAW也可以
处理特殊的IPV4报文；此外利用原始套接字，可以通过IP_HARINCL套接字选择由用户伪造IP头
socket.SOCK_RAW 通常仅限于搞基用户或管理员运行的程序使用
socket.SOCK_RDM 是一种可靠的UDP形式，即保证交付数据报但不保证顺序。
socket.SOCK_SEQPACKET 可靠的连续数据包服务
socket 函数
socket(family,type[,protocal]) 使用给定的地址簇，套接字类型，协议编号来创建套接字
s.bind(address) 
s.listen(backlog) 开始监听传入连接，backlog指定在拒绝连接之前,操作系统可以挂起的最大连接数，至少为1，一般为5
s.connect(address) 连接失败返回socket.error
s.accept() 接受连接并返回(conn,address),conn是新的套接字对象，可以用来接收和发送数据
accept()方法在有新连接进入时就会返回conn,addr这两个变量，但如果没有连接时，此方法就会阻塞直至有新连接过来
address 是连接客户端的地址，如('192.168.36.131', 30786)
conn.recv(1024) 接收数据
conn.sendall(data) 发送数据
strip()    去掉行首和行尾的空格
SocketServer 模块支持多线程
SocketServer简化了网络服务器的编写。它有4个类：TCPServer，UDPServer，UnixStreamServer，UnixDatagramServer。这4个类是同步进行处理的，另外通过ForkingMixIn和ThreadingMixIn类来支持异步。 创建服务器的步骤。首先，你必须创建一个请求处理类，它是BaseRequestHandler的子类并重载其handle()方法。其次，你必须实例化一个服务器类，传入服务器的地址和请求处理程序类。最后，调用handle_request()(一般是调用其他事件循环或者使用select())或serve_forever()...
ThreadingMixIn 异步通信
python 时间转换
import time
time.strptime('20160224 14:20:00','%Y%m%d %H:%M:%S')  对时间进行格式化
time.mktime(time.strptime('20160224 14:20:00','%Y%m%d %H:%M:%S'))   转换为时间戳
time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat('/etc/passwd').st_atime))    时间戳转换为标准时间
多线程
import threading
def run(arg):    //定义线程执行的函数
    pass
p_list =[]
for in range(10):
    t = threading.Thread(target=run,args=(arg,))    //定义线程
    t.start()    //启动线程
    p_list.append(t)    //把启动的线程添加到列表中，避免线程的串行运算
for p in p_list:
    p.join()    //等待线程执行完毕

main_thread = threading.Thread(target=main,args=(10,))
main_thread.setDaemon(True)    //把main_thread设置为守护线程

event = event.Event()
event.wait()    //如果标志位已设定，不做任何事，等待标识位被设定
event.set()
event.isSet()    不阻塞
event.clear()    

生成者消费者模型
Queue
q = Queue.Queue()    //生成一个队列，先进先出
q.put()
q.get() 阻塞
q.qsize()    队列的数量
q.get_nowait()    非阻塞
q.clear()    清除queue

多进程
import multiprocessing
p = multiprocessing.Process(traget=run,args=(arg,))    封装进程
p.start()    启动进程
p.join()    等待线程结束

进程池
Pool = multiprocessing.Pool(process=5)    定义在进程池中启动多少个进程
for in range(10):    //启动了10个进程
    Pool.apply_async(run,args=(arg,))    

Pipe 管道
m = multiprocessing.Manager()
name_dic = m.dict()    共享一个字典
多进程中的lock，限制多个进程对同一个文件的操作

select
select     vs     poll     最大文件监控数量
1024            无限制
 epoll     返回活动的句柄给用户进程
difflib模块实现对比连个文件的内容，可以生产html格式的文件，方便进行查看
生产html格式文件
d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)
filecmp 可以实现文件、目录、遍历字目录的差异对比功能
filecmp 提供了三个操作方法: cmp(单文件对比)、cmpfiles(对文件对比)、dircmp(目录对比)
filecmp.cmp(f1,f2[,shallow])    相同返回true，不同返回false shallow默认是true，根据os.stat()方法返回的文件基本信息进行对比
当shallow 为false 时，则os.stat(）与文件内容同上进行校验
filecmp.cmpfiles(dir1,dir2,对比文件类别)，返回三个列表匹配，不匹配，错误(不存在的文件或无法对比的文件)
如果你要用python匹配字符串的开头或末尾是否包含一个字符串，就可以用startswith 和 endswith
例如: content = 'ilovepython'
如果字符串content以ilove开始，返回True，否则返回False
则可以用这句脚本进行判断:  if content.startswith("ilove") :
一个decorator，所以接受一个函数作为参数，并返回一个函数
把@log放到now()函数的定义处，相当于执行了语句now = log(now)
int()函数可以将浮点数转换为整数，但是不做四舍五入操作，而是直接去掉小数部分
help()函数是查看函数或模块用途的详细说明，而dir()函数是查看函数或模块内的操作方法都有什么，输出的是方法列表
解释器简介，它的作用是将我们编写的源代码，转换翻译成机器可以读的懂的字节码，最后交给中央处理器来执行命令
%r是repr；%s是str；前者是被repr处理后的string对象，后者直接是string对象
s = {'one':1,'two':2,'three':3}
print s
m = iter(s)    //iter()函数
print m.next()
print m.next()
print m.next()
结果:
{'three': 3, 'two': 2, 'one': 1}
three
two
one
xrange做循环的性能比range好，尤其是返回很大的时候。尽量用xrange吧，除非你是要返回一个列表
xrange 按需分配
字符串操作
s=" this is a test "
s.lower()    全部转换为小写
s.upper()    全部转换为大小
s.capitalize()    仅把每行的首字母大写
s.swapcase()    大小写互换
s.title() 把每个单词的首字母大写
s.find('i') 用find方法来查找子串‘I’，如果找到就返回匹配的第一个索引值。
s.count('a')    查找子串在字符串中的匹配次数
s.replace('a','b')    字符串替换
s.strip('aa')    strip()方法作用是删除头部和尾部的匹配字符
strip()方法还有几个近亲，lstrip()与rstrip()，左边匹配删除，和右边匹配删除，一般我们用这些功能是删除空格、回车等
没有用global语句的情况下，是不能修改全局变量的
python并行遍历zip()函数使用方法:
a = [1,2,3]
b = [4,5,6]
zip(a,b)
[(1, 4), (2, 5), (3, 6)]
Python程序调用自身的这种方法叫做递归，如果达不到我们需要的条件，而它会永远的继续递归调用下去，而程序也会永远不停止，这种现象叫做Python的无限递归
==比较操作符：用来比较两个对象是否相等，value做为判断因素；
is同一性运算符：比较判断两个对象是否相同，id做为判断因素
id(身份标识)、 type()(数据类型)
位置参数:def x(name,Profession) print x(Profession='Student',name='Amy')
关键字参数:def a1(x,y,z) a1(1,2,3)
作为实参传入到函数的变量名称和函数定义里形参的名字没有关系。函数里面只关心形参的值，而不去关心它在调用前叫什么名字
Python函数的两种类型参数，一种是函数定义里的形参，一种是调用函数时传入的实参
序列中的每一个元素都有自己的位置编号，可以通过偏移量索引来读取数据。最开始的第一个元素，索引为0，第二个元素，索引为1，以此类推；也可以从最后一个元素开始计数，最后一个元素的索引是-1，倒数第二个元素的索引就是-2，以此类推
什么是切片：切片简单的来说就是取出一个范围内的元素。
>>> x[4:-4]
序列相加：相同数据类型序列之间可以相加，不同数据类型序列不能相加
序列乘法：把原序列乘X次，并生成一个新的序列
成员资格：检查某个指定的值是否在序列中，用in布尔运算符来检查，其返回值为True/False。True为真，在这里可以理解为要查找的值在序列中，False结果与其相反
序列内建函数：len()函数计算序列内元素数量；min()函数、max()函数分别查找并返回序列中的最大或最小元素
assert 断言句语格式及用法很简单。在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助
assert 表达式 [, 参数]
列表排序方法有三个：reverse反转/倒序排序、sort正序排序、sorted可以获取排序后的列表。在更高级列表排序中，后两中方法还可以加入条件参数进行排序
reverse列表反转排序：是把原列表中的元素顺序从左至右的重新存放，而不会对列表中的参数进行排序整理。如果需要对列表中的参数进行整理，就需要用到列表的另一种排序方式sort正序排序
sort()此函数方法对列表内容进行正向排序，排序后的新列表会覆盖原列表（id不变），也就是sort排序方法是直接修改原列表list排序方法。
sorted()函数即可以保留原列表，又能得到已经排序好的列表
len(list)    //列表中元素的个数
list.count('元素')    //列表中某个元素出现的次数
求模操作符应用在Python的整数类型上，用来计算出第一个操作数除以第二个操作数的余数，这个求模操作符在Python里面是一个 “%”号
file.seek() 移动游标
file.tell()    显示当前游标的位置
file.seek(5,1)    移动5个字节，1表示当前位置开始，0表示开头，2表示结尾
file.seek()方法标准格式是：seek(offset,whence=0)
offset：开始的偏移量，也就是代表需要移动偏移的字节数
whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起
datetime 导入日期模块
today=datetime.date.today()
yesterday = today - datetime.timedelta(days=1) #用今天日期减掉时间差，参数为1天，获得昨天的日期
网页爬虫出现乱码的情况，页面编码是gb2312
print html.read().decode('gbk').encode('utf-8') 
urllib.urlretrieve(url,'/tmp/test.html')    把一个网页的内容保存到本地文件中
转义符\r就可以把光标移动到行首而不换行，转义符\n就把光标移动到行首并且换行
格式运算符%
%c 转换成字符
%s %d
%% 输出%
def func(args1,*argst):  #多个参数
    print args1
    print argst
列表去重 
ids = [1,4,3,3,4,2,3,4,5,6,1]
ids = list(set(ids))
python类
class Student(object):
    count = 0
    books = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

wilber = Student("Wilber", 28)
wilber.gender = "male" 添加一个实例属性
在上面的Student类中，”count””books””name”和”age”都被称为类的数据属性，但是它们又分为类数据属性和实例数据属性
对于类数据属性和实例数据属性，可以总结为：
类数据属性属于类本身，可以通过类名进行访问/修改 Student.books.extend(["python", "javascript"])  
类数据属性也可以被类的所有实例访问/修改  
在类定义之后，可以通过类名动态添加类数据属性，新增的类属性也被类和所有实例共有 Student.hobbies = ["reading", "jogging", "swimming"]
实例数据属性只能通过实例访问
在实例生成后，还可以动态添加实例数据属性，但是这些实例数据属性只属于该实例
特殊的类属性:
__name__	类的名字（字符串）
__doc__	类的文档字符串
__bases__	类的所有父类组成的元组
__dict__	类的属性组成的字典
__module__	类所属的模块
__class__	类对象的类型
虽然通过实例可以访问类属性，但是不建议这么做，最好还是通过类名来访问类属性
在一个类中，可能出现三种方法，实例方法、静态方法和类方法
实例方法:
实例方法的第一个参数必须是”self”,实例方法只能通过类实例进行调用，这时候”self”就代表这个类实例本身
类方法:
类方法以cls作为第一个参数，cls表示类本身，定义时使用@classmethod装饰器。通过cls可以访问类的相关属性
类方法可以通过类名访问，也可以通过实例访问
静态方法:
与实例方法和类方法不同，静态方法没有参数限制，既不需要实例参数，也不需要类参数，定义的时候使用@staticmethod装饰器
同类方法一样，静态法可以通过类名访问，也可以通过实例访问
这三种方法的主要区别在于参数，实例方法被绑定到一个实例，只能通过实例进行调用；但是对于静态方法和类方法，可以通过类名和实例两种方式进行调用
在Python中，通过单下划线”_”来实现模块级别的私有化，一般约定以单下划线”_”开头的变量、函数为模块私有的，也就是说”from moduleName import *”将不会引入以单下划线”_”开头的变量、函数
对于Python中的类属性，可以通过双下划线”__”来实现一定程度的私有化，因为双下划线开头的属性在运行时会被”混淆”（mangling）
”__address”属性在运行时，属性名被改为了”_Student__address”（属性名前增加了单下划线和类名）
双下划线的另一个重要的目地是，避免子类对父类同名属性的冲突
“_”：以单下划线开头的表示的是protected类型的变量，即只能允许其本身与子类进行访问；同时表示弱内部变量标示，如，当使用”from moduleNmae import *”时，不会将以一个下划线开头的对象引入。
“__”：双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了，连子类也不可以，这类属性在运行时属性名会加上单下划线和类名
Python中属性的获取 我们通常采用类.属性或实例.属性的形式调用
Python中属性的设置 对于属性的设置我们通常采用类.属性 = 值或实例.属性 = 值的形式
Python中的属性设置:
obj.aaa += 2包含了属性获取及属性设置两个操作
第一个操作 赋值操作obj1.aaa += 2等价于obj1.aaa = obj1.aaa + 2
第二个操作是属性设置，即obj.aaa = 12。当发生属性设置的时候，obj1这个实例对象没有属性aaa，因此会为自身动态添加一个属性aaa
Python中的属性获取是按照从下到上的顺序来查找的 实例对象--类对象
Python中的类和实例是两个完全独立的对象且Python中的属性设置是针对对象本身进行的
python2.x和3.x版本中都存在的并且功能并不齐全的函数:distutils.log.warn() 代理了print 和print()两种方式
from distutils.log import warn as printf
    printf(xxxxx)
套接字有两种类型:基于文件的和面向网络的
Unix套接字是我们所讲的套接字的第一个家族，AF_UNIX 表示地址家族 address family:unix
基于网络的套接字也有自己的家族名字 AF_INET
套接字地址:主机---端口对
有效的端口号0~65535
面向连接的套接字和无连接的套接字
面向连接的:TCP 需要使用sock_stream 作为套接字类型
无连接的:UDP 需要使用sock_dgram 作为套接字类型
ftp有主动和被动模式两种，只有在主动模式下服务器才使用数据端口，在服务器把20号端口设置为数据端口后，它"主动"连接客户端的数据端口。而在被动模式下，服务器只是告诉客户端随机的数据端口号，客户端必须主动建立数据连接
POP(Post Office Protocal)邮局协议 IMAP(Internet Message Access Protocal) 互联网邮件访问协议
poplib 模块 类 poplib.POP3
poplib.POP3_SSL类，提供一些凭证信息用于加密连接传输邮件
python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
Python中assert用来判断语句的真假，如果为假的话将触发AssertionError错误
a = 23
assert a == 23
处理xml所用到的模块 xml.sax xml.dom xml.ElementTree
多线程编程
进程则是一个执行中的程序，每个进程都拥有自己的地址空间、内存、数据栈以及其他跟踪执行的辅助数据。进程也可以通过派生新的
进程来执行其他任务，每个新进程都拥有属于自己的内存和数据栈，所有只能采用进程间通信(IPC)的方式共享信息
python代码的执行是由python虚拟机进行控制的，尽管Python解释器中可以进行多个线程，但是在任意给定时刻只有一个线程会被解释器执行，对Python虚拟机的访问是由全局解释器锁(GIL)控制的,这个锁就是用来保证同时只有一个线程运行。
Python虚拟机将按照下面所述的方式执行:
1.设置GIL
2.切换进一个线程去运行
3.执行下面操作之一
    a.指定数量的字节码指令
    b.线程主动让出控制权(可以调用time.sleep(0))来完成
4.把线程设置回睡眠状态(切换出线程)
5.解锁GIL
6.重复上述步骤
退出线程可以通过sys.exit()
不建议使用thread模块，主线程退出后，所有其他线程都会在没有清理的情况下直接退出
threading模块会确保所有"重要的"子线程退出前，保持整个进程的存活
主线程应该做好一个管理者，负责了解每个单独的线程需要执行什么，每个派生的线程需要哪些数据或参数，这些线程执行完成后会提供什么结果，这样主线程就可以收集每个线程的结果，然后汇总成一个有意义的最终结果
在线程应用中使用queue模块，用户可以创建一个队列数据结构，用于在多线程之间的数据共享
*args表示任何多个无名参数，它是一个tuple
**kwargs表示关键字参数，它是一个dict
首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗，不要搞另类，大家会不明白的
self代表类的实例，而非类
利用2to3可以实现Python2.x版本的代码到3.x的转换
使用from atexit import register ，atexit.register()来注册_atexit()函数，以便让解释器在脚本退出前执行该函数
类中self的具体含义
class Form(QDialog):
   ........
   amountLabel = QLabel("Amount")
   self.amountLabel = QLabel()
   ........
python中的类中属性元素加self.和不加self.的区别是什么？这两个变量都在类定义中
如果不加self，表示是类的一个属性（可以通过“类名.变量名”的方式引用），加了表示是类的实例的一个属性（可以通过“实例名.变量名”的方式引用）。
class是模子，instance是用模子刻出来的东西
class是共性，instance是基于class的共性实现出来的具体的某个东西（对象）
instance是从class生出来的
类：方法(类中的函数) 类的属性(类中的变量)
实例:instance是基于class实现出来的具体的某个东西（对象）
对象方法，对象的变量
Python中self的含义:
self，英文单词意思很明显，表示自己，本身。
此处有几种潜在含义：
1.这里的自己，指的是，实例Instance本身
2.同时， 由于说到“自己”这个词，都是和相对而言的“其他”而说的。
而此处的其他，指的是，类Class，和其他变量，比如局部变量，全局变量等。
此处的self，是个对象，Object。
是当前类的实例。
因此，对应的
self.valueName
self.function()
中的
valueName：表示self对象，即实例的变量。与其他的，Class的变量，全局的变量，局部的变量，是相对应的。
function：表示是调用的是self对象，即实例的函数。与其他的全局的函数，是相对应的
Python中__init__的含义:
不同的示例，在初始化的时候，都传递一个对应的参数，这样不同的Person，就都有了自己的不同的名字了
当一个Class，稍微复杂一点的时候，或者内部函数需要用得到的时候，往往都需要在，别人实例化你这个类之前，使用你这个类之前，做一些基本的，与自己的类有关的，初始化方面的工作。
而这部分工作，往往就放到__init__函数中去了。
换句话说，你要用人家的类（中的变量和函数）之前，总要给人家一个机会，做点准备工作，然后才能为你服务吧
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self
假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法MyObject.method(arg1, arg2)的时候，这会由Python自动转为MyClass.method(MyObject, arg1, arg2)
self指的是类实例对象本身(注意：不是类本身)
如果self指向类本身，那么当有多个实例对象时，self指向哪一个呢？
Python中if __name__ == '__main__' 的具体含义:
1.当单独执行该module时，比如单独执行以上hello.py，可以理解为"if __name__=="__main__":" 这一句与c中的main()函数所表述的是一致的，即作为入口
2.当该module被其它module 引入使用时，其中的"if __name__=="__main__":"所表示的Block不会被执行,这是因为此时module被其它module引用时，其__name__的值将发生变化，__name__的值将会是module的名字
3.因此，在python中，当一个module作为整体被执行时,moduel.__name__的值将是"__main__"；而当一个module被其它module引用时，module.__name__将是module自己的名字，当然一个module被其它module引用时，其本身并不需要一个可执行的入口main了
4.这个脚本被执行的时候，__name__ 值就是 __main__ ，才会执行 main()函数 ，如果这个脚本是被 import 的话，__name__的值不一样。main()函数就不会被调用。 这个句子用来写既能直接运行，又能给其他python程序import，提供库调用的脚本
5.解释下__name__：每一个模块都有一个内置属性__name__。而__name__的值取决与python模块（.py文件）的使用方式。如果是直接运行使用，那么这个模块的__name__值就是“__main__”；如果是作为模块被其他模块调用，那么这个模块（.py文件）的__name__值就是该模块（.py文件）的文件名，且不带路径和文件扩展名
6.__name__系统变量指示模块应如何被加载，他的值为"__main__"时表示当前模块是被直接执行。
由于主程序代码无论模块是被导入还是直接被执行都会运行，所以我们需要一种方式在运行时检测该模块是被导入还是被直接执行。该方式也就是__name__系统变量。如果模块是被导入，__name__的值为模块名字；如果是被直接执行，__name__的值为"__main__"
id(object)功能：返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。此处所说的对象应该特指复合类
一个对象的id值在CPython解释器里就代表它在内存中的地址（Python的c语言实现的解释器）
用is判断两个对象是否相等时，依据就是这个id值
is与==的区别就是，is是内存中的比较，而==是值的比较
python每日一函数 - divmod数字处理函数
divmod(a,b)函数
中文说明：
divmod(a,b)方法返回的是a//b（除法取整）以及a对b的余数
返回结果类型为tuple
divmod(9,2) 结果 (4, 1)    divmod(1, 4)结果(0,1)
dir()函数
使用内建的dir函数来列出模块定义的标识符。标识符有函数、类和变量
为dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当前模块中定义的名称列表
delattr(object, name)中文说明：删除object对象名为name的属性 
delattr(tom, "age") #删除对象tom中的age属性
complex([real[, imag]]) 参数real: int, long, float或字符串； 参数imag: int, long, float
compile(source, filename, mode[, flags[, dont_inherit]])中文说明：将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值
cmp(x, y) 比较两个对象x和y，如果x < y ,返回负数-1；x == y, 返回0；x > y,返回正数 1。 
该函数只有在python2中可用，而且在python2所有版本中都可用。但是在python3中该函数已经被删减掉
classmethod是用来指定一个类的方法为类方法，没有此参数指定的类的方法为实例方法，使用方法如下：
class C: 
    @classmethod
    def f(cls, arg1, arg2, ...): ...
类方法既可以直接类调用(C.f())，也可以进行实例调用(C().f())
类中的实例方法定义第一个参数必须是self，而普通函数（不在类中）的定义没有self参数
self 指的是你定义的这个类被调用创建了一个实例时，self就是这个实例
1、如果你需要用实例来调用你的方法，那么在定义方法的时候，一定要把第一个参数设置成为self；
2、如果你需要使用静态方法，那么你需要在方法前面加上@staticmethod修饰符；
    @staticmethod
    def f1(arg): #here is a static method. it's not necessary  只一个参数
3、如果要使用类方法，那么你需要在方法前面加上@classmethod修饰符，并且在方法中至少使用一个参数，第一个参数在方法中的作用就是代表改类本身
    @classmethod
        def f2(cls, arg): #here is a class method. you have to take  第一个参数为类
chr(i) 返回整数i对应的ASCII字符。与ord()作用相反
bool(x) 把x转换为boolen类型
Python中除了''、""、0、()、[]、{}、None为False之外，其他的都是True
bin(x) 将整数x转换为二进制字符串，如果x不为Python中int类型，x必须包含方法__index__()并且返回值为integer
 bin(521)
#这里的显示结果形式与我们平时习惯有些差别，主要是前面多了0b，这是表示二进制的意思。
'0b1000001001'
basestring() 可以被用来判断一个对象是否为str或者unicode的实例，isinstance(obj, basestring) python2.3以后python2各版本。注意：python3中舍弃了该函数
>>> isinstance("Hello world", basestring)
True
>>> isinstance(u"你好", unicode)
True
abs() 返回绝对值 
any() 当可迭代对象中有任意一个不为False，则返回True
all() 当可迭代对象中有任意一个不为True，则返回False
在JSON中，有两种结构：对象和数组
一个对象以"{"（左括号）开始，"}"（右括号）结束。每个"名称"后跟一个":"（冒号）；"'名称/值’'对"之间运用 “,”（逗号）分隔。 名称用引号括起来；值如果是字符串则必须用括号，数值型则不须要
var o={
   "xlid":"cxh",
   "xldigitid":123456,
   "topscore":2000,
}；
数组是值（value）的有序集合。一个数组以”[”（左中括号）开始，"]"（右中括号）结束。值之间运用 ","（逗号）分隔
在数据传输流程中，json是以文本，即字符串的形式传递的，而JS操作的是JSON对象，所以，JSON对象和JSON字符串之间的相互转换是关键
可以运用 toJSONString()或者全局的JSON.stringify()函数将JSON对象转化为JSON字符串
//将JSON对象转化为JSON字符
var last=obj.toJSONString();
//将JSON对象转化为JSON字符
var last=JSON.stringify(obj);
在数据传输流程中，json是以文本，即字符串的形式传递的；
Json.stringify()将JSON对象转为JSON字符串（序列化）；
Json.parse()将JSON字符串转为JSON对象（反序列化）；
字典转换为json对象，主要是利用json.dumps()函数
>>> dir = {'name':'tony','age':31,'salary':1000000}
>>> str = json.dumps(dir)
>>> print str
{"salary": 1000000, "age": 31, "name": "tony"}
在json的编码过程中，会存在从python原始类型向json类型的转换过程，具体的转换 利用的是json.dumps()
    如下：
        python      -->           json
        dict                      object
        list,tuple                array
        str,unicode               string
        int,long,float            number
        True                      true
        False                     false
        None                      null
test_dump = json.dumps(testA, sort_keys = True, indent = 4) indent参数是缩进的意思
   而json转换为python类型的时候，调用的是json.loads()方法，按照如下规则转换的：
        json        -->           python
        object                    dict
        array                     list
        string                    str
        number(int)               int
        number(real)              float
        true                      True
        false                     False
        null                      None
# Converting Python to JSON
json_object = simplejson.dumps( python_object )
# Converting JSON to Python
python_object = simplejson.loads( json_object )
python从web接口上查询信息得到的是json结构的数据，利用json.dumps()进行转换成Python的字典或者列表，然后进行数据获取
首先，json基本上是key/value的，python中就叫字典。既然是字典，那就应该安照读字典的方式去读。 将上面的data转为字典类型，这里用json模块的read方法
# Writing JSON data 
with open('data.json', 'w') as f:   json.dump(data, f)
# Reading data back 
with open('data.json', 'r') as f:   data = json.load(f)
python中不同的类型要用不同的锁，多线程使用类中的共同数据时一定要加锁，类中的方法参数最好不要用self
在上面所示的完整语句中try/except/else/finally所出现的顺序必须是try-->except X-->except-->else-->finally，即所有的except必须在else和finally之前，else（如果 有的话）必须在finally之前，而except X必须在except之前。否则会出现语法错误
try/except完整格式而言，else和finally都是可选的，而不是必须的，但是如果存在的话else必须在finally之前，finally（如果存在的话）必须在整个语句的最后位置
else语句的存在必须以except X或者except语句为前提，如果在没有except语句的try block中使用else语句会引发语法错误。也就是说else不能与try/finally配合使用
XML 指可扩展标记语言（eXtensible Markup Language）
python有三种方法解析XML，SAX，DOM，以及ElementTree
SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件
SAX是一种基于事件驱动的API
利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器
解析器负责读取XML文档,并向事件处理器发送事件,如元素开始跟元素结束事件;
而事件处理器则负责对事件作出相应,对传递的XML数据进行处理。
引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler

DOM 文件对象模型 将XML数据在内存中解析成一个树，通过对树的操作来操作XML
ElementTree(元素树):ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少
注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）
read()会读取整个文件，将读取到底的文件内容放到一个字符串变量，返回str类型
read(size) 读入指定大小的内容，以byte为单位，size为读入的字符数，返回str类型
readline()读取一行内容，放到一个字符串变量，返回str类型
readlines() 读取文件所有内容，按行为单位放到一个列表中，返回list类型
for parent,dirnames,filenames in os.walk(basedir):
字符传格式化函数 format 2.6以后
str.format() 用{}和: 代替%
'{1}.{2} | {0}.{1}.{2}'.format('www', 'pythontab', 'com')
'pythontab.com | www.pythontab.com'
'{domain} ### {year}'.format(year=2016,domain='www.pythontab.com')
'www.pythontab.com ### 2016'
'{0[1]}.{0[0]}.{1}'.format(['pyhtontab', 'www'], 'com')
'www.pyhtontab.com'
它有着丰富的的“格式限定符”（语法是{}中带:号），比如：
填充与对齐
填充常跟对齐一起使用
^、<、>分别是居中、左对齐、右对齐，后面带宽度
:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
'{:0>10}'.format(2016)
'0000002016'
'{:.2f}'.format(2016.0721)
'2016.07'
b、d、o、x分别是二进制、十进制、八进制、十六进制
'{:o}'.format(2016)
'3740'
字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码
decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码
在Python中，tuple是不可变对象，但是这里的不可变指的是tuple这个容器总的元素不可变（确切的说是元素的id），但是元素的值是可以改变的
默认参数跟函数调用次数无关，仅仅在函数定义的时候被初始化一次
raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来
raw_input() 将所有输入作为字符串看待，返回字符串类型。而 input() 在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（ int, float ）；同时在例子 1 知道，input() 可接受合法的 python 表达式，举例：input( 1 + 3 ) 会返回 int 型的 4
input() 本质上还是使用 raw_input() 来实现的，只是调用完 raw_input() 之后再调用 eval() 函数
除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互
使用zip同时遍历两个列表
for cat, dog in zip(cats, dogs):
print(cat, dog)
同时考虑列表变量的索引和值，可以使用enumerate：
for index, cat in enumerate(cats):
print(cat, index)
永远不要使用可变的默认参数
python3 使用PyMysql连接数据库
Python随机数与随机字符串详解
import random
random.randint(0,99) 取整数
random.randrange(0,101,2) 取偶数
random.random() 随机浮点数
random.choice('adaf2jfakld') 随机字符
random.sample('ajflakdjfkl',3) 多个字符中随机选取特定数量的字符
random.shuffle( [1, 2, 3, 4, 5, 6] ) 对列表洗牌
import datetime
# #如果是返回当前时间，可以简单的写成
# # time.localtime()
# # #这个返回UTC时间
# # time.gmtime()
# lt = time.localtime()
# tm = time.gmtime()
# ft = time.strftime('%Y-%m-%d %H-%M',lt)
# ft2 = time.strftime('%Y-%m-%d %H:%M',tm)
# print ft, ft2
# print '--------------------------------------------------------'
# now = datetime.datetime.now()
# now = now.replace(day = 1)
# print now
# print now.time()
#
# mytime = ['2014-09-06 20:19']
# #mytime2 = '2014-10-09 14:32'
# str = "".join(mytime)
# print str
# retime  = datetime.strptime(str,'%Y-%m-%d %H:%M')
# print retime
# retime = retime +timedelta(hours = 8)
# print retime
#
# tdtime = datetime.now()
# print tdtime
# if retime <= tdtime - timedelta(days = 7):
#     print "too early"
python 的时间转换 time模块中的striptime() 和strftime()
strptime()    根据你指定的格式控制字符串解读日期
strftime()    根据你指定的格式控制字符输出日期
isinstance(object, classinfo)  classinfo 处可以是 a class, type, or tuple of classes and types
字符串类型的判断分为strunicode，二者均继承自 basestring
 isinstance(u'3.0', unicode)
True
>>> isinstance('3.0', str)
True
数字的类型判断数字分为 int 和 float，暂未发现二者共同的有效父类
 isinstance('3', (int, float))
False
>>> isinstance(3.0, (int, float))
True
time.time() 当前时间的秒数
time.ctime([sec])#把秒数转换成日期格式，如果不带参数，则显示当前的时间
对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）
但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）
encode 和 decode在pyhton 中的意义可表示为
                              encode
unicode -------------------------> str
unicode <--------------------------str
                              decode
又有人要问如何忽略命令行下警告错误的输出呢 python -W ignore yourscript.py
F.truncate([size])  把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置
Structlog是一个先进的日志记录处理器
Watchdog是一个跨平台的Python库和shell工具，可以监视文件系统事件
Requests，或称为人类使用的HTTP，是一个处理HTTP请求更为pythonic 的方法，比urllib2更更更好用
lxml是libxml2和libxslt的合体
 filter(function, sequence)
对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回。
map(function, sequence)
对sequence中的item依次执行function(item)，见执行结果组成一个List返回：
map也支持多个sequence，这就要求function也支持相应数量的参数输入
拆分中英文混合字符串
#coding=utf-8
import re
s = 'hi新手oh'.decode('utf-8') #举个栗子是字符串s，为了匹配下文的unicode形式，所以需要解码
p = re.compile(ur'[\u4e00-\u9fa5]') #这里是精髓，[\u4e00-\u9fa5]是匹配所有中文的正则，因为是unicode形式，所以也要转为ur     
print p.split(s) #使用re库的split切割
不论传入的参数的原始类型是什么，one(*x)在*x的位置接收这些传入的参数后，都会将其保存成"元组"，而元组是不能改变的
实际上，单星号是无法读取到字典中的值的，永远只会读取到字典中的键，如果想读取到字典中的值，需要使用双星号
#对一个字典使用双星号前缀，就相当于将其拆分成关键字参数的形式，**dect相当于将字典拆分成下面这种样子
one=1,two=2,three=3
#将上面这些关键字参数传入one(**x)，就等价与（还记得前面说的，双星号将接收到的所有关键字参数都保存成一个字典吧）
one({"one":1,"two":2,"three":3})
在一个函数的接收参数中，同时出现"非关键字参数（位置参数）"和"关键字参数"时，可以使用一个单星号来分隔这两种参数，例如：
def mix(a,b,*,x,y):
  """位置参数与关键字参数混合"""
  return a,b,x,y
#星号前面的a和b是位置参数，星号后面的x和y是关键字参数，调用mix()函数并传入参数时，关键字参数一定要使用"变量名=值"的形式传入数据，如果同位置参数一样传入数据，就会引发一个TypeError异常
print(mix(1,2,x=3,y=4))
如果位置参数与关键字参数之间已经存在了一个单星号位置参数，那么，这个参数后面的就都是关键字参数，也不需要再使用星号来分隔他们了
Python把以两个或以上下划线字符开头且没有以两个或以上下划线结尾的变量当作私有变量。私有变量会在代码生成之前被转换为长格式（变为公有）。转换机制是这样的：在变量前端插入类名，再在前端加入一个下划线字符。这就是所谓的私有变量轧压（Private name mangling）。如类 A里的__private标识符将被转换为_A__private
通过实例a修改类的属性并不会修改类属性的值，只是增加了一个实例属性
实例的作用域发生变化，并不会影响到该类的其它实例，但是类的作用域发生变化，则会影响到该类的所有实例
python中for循环可用于任何“可迭代对象”，这其实就是迭代器
迭代器一个显而易见的好处就是：每次只从对象中读取一条数据，不会造成内存的过大开销
生成器函数在Python中与迭代器协议的概念联系在一起。简而言之，包含yield语句的函数会被特地编译成生成器。当函数被调用时，他们返回一个生成器对象，这个对象支持迭代器接口。函数也许会有个return语句，但它的作用是用来yield产生值的
不像一般的函数会生成值后退出，生成器函数在生成值后会自动挂起并暂停他们的执行和状态，他的本地变量将保存状态信息
def fab(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a+b
for i in fab(5):
 print i
字符串在Python内部的表示是unicode 编码，因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码
python删除文件及目录
os.remove() 删除文件
os.rmdir()删除空目录
os.removedirs() 递归删除空目录
递归删除目录和文件
for root,dirs,file in os.walk()
利用shutil进行批量删除
import shutil
shutil.rmtree()
python的关键字参数和非关键字参数 
def foo1(arg1,arg2,key1=1,key2=2,*arg,**keywords):
arg1,arg2，key1，key2普通参数
*arg 非关键字参数列表
**keywords 关键字参数列表
对文件的访问方式一般有三种模式：读模式（'r'）、写模式（'w'）或追加模式（'a'）.  另外两种可混合使用的模式: 二进制模式（‘b’）,读/写模式（‘+’）
from math import sqrt是把sqrt作为本文件的方法导入进来了，使用的时候只需要直接调用sqrt
import是import math，那么调用的时候要采用math.sqrt的方式
s=[1,2,3,4]       # S 上界为 0 下界为 4
s[-100:100]       #返回 [1,2,3,4] -100超出了上界，100超出了下界：等价于 s[0:4]
s[-100:-200]      #返回 [] -100,-200均超出了上界，自动取上界：等价于s[0:0]
s[100:200]        #返回 [] 100,200均超出了下界，自动取下界值：等价于s[4:4]
s[:100]           #返回 [1,2,3,4] 开始值省略表示从第0个开始
s[0:]             #返回 [1,2,3,4] 结束值为空表示到最后一个结束
list的切片，内部是调用__getitem__，__setitem__,__delitem__和slice函数。而slice函数又是和range()函数相关的。
给切片传递的键是一个特殊的slice对象。该对象拥有可描述所请求切片方位的属性
filter很容易理解用于过滤，map用于映射，reduce用于归并 都是对一个集合进行处理
filter()函数:对集合中的元素进行过滤
map():对集合中的元素进行改变，+ - * /
reduce():二元函数 reduce(lambda x,y:x+y,a)
字典的基本操作
has_key() 判断是否存在key
clear() 清空字典
copy()字典的复制
update()更新字典中的某个值
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作
参数前加一个星号，表明将所有的值放在同一个元组中，该参数的返回值是一个元组。
参数前加两个星号，表明将所有的值放在同一个字典中，该参数的返回值是一个字典
全部大写：str.upper()
   全部小写：str.lower()
   大小写互换：str.swapcase()
   首字母大写，其余小写：str.capitalize()
   首字母大写：str.title()
获取固定长度，右对齐，左边不够用空格补齐：str.rjust(width)    
   获取固定长度，左对齐，右边不够用空格补齐：str.ljust(width)
   获取固定长度，中间对齐，两边不够用空格补齐：str.center(width)
   获取固定长度，右对齐，左边不足用0补齐    str.zfill(20)
 搜索指定字符串，没有返回-1：str.find('t')
   指定起始位置搜索：str.find('t',start)
   指定起始及结束位置搜索：str.find('t',start,end)
   从右边开始查找：str.rfind('t')
   搜索到多少个指定字符串：str.count('t')
   上面所有方法都可用index代替，不同的是使用index查找不到会抛异常，而find返回-1
字符串替换相关 替换old为new：str.replace('old','new')
去两边空格：str.strip()
   去左空格：str.lstrip()
   去右空格：str.rstrip()
字符串判断相关
   是否以start开头：str.startswith('start')
   是否以end结尾：str.endswith('end')
   是否全为字母或数字：str.isalnum()
   是否全字母：str.isalpha()
   是否全数字：str.isdigit()
   是否全小写：str.islower()
   是否全大写：str.isupper()
   str='python String function'
列表的复制 b = a[:]
通过内置方法id()来查看对象的地址
zip()配合*号操作符,可以将已经zip过的列表对象解压
result =  [(1, 4), (2, 5), (3, 6)]
zip(*result)  [(1, 2, 3), (4, 5, 6)]
不论传入的参数的原始类型是什么，one(*x)在*x的位置接收这些传入的参数后，都会将其保存成"元组"，而元组是不能改变的
实际上，单星号是无法读取到字典中的值的，永远只会读取到字典中的键，如果想读取到字典中的值，需要使用双星号
dect={"one":1,"two":2,"three":3}
one(**dect)
对一个字典使用双星号前缀，就相当于将其拆分成关键字参数的形式，**dect相当于将字典拆分成下面这种样子
one=1,two=2,three=3
如果我们要在一个函数中包含多种参数的组合，必须遵守这样的顺序：位置参数（必选参数），默认参数，单星号参数或星号分隔符，关键字参数，双星号参数；
开发中遇到一个问题，python中判断一个字符串是否为数字，在网上搜索了半天，找到两种方法：
str(value).isdigtal()
unicode(str(value)).isdecimal()
可是上面两种都判断小数，如"3.4"  不是数字，判断整数是可以的，但是判断小数有问题。
python datetime获取几分钟、小时、天之前的时间
print ((datetime.datetime.now()-datetime.timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M"))
可以控制days、seconds、minutes、hours、weeks等
把时间转换为时间戳 
将格式字符串转换为时间戳
  a = "Sat Mar 28 22:24:24 2009"
  b = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
文件操作 a 追加文件内容
"r"   以读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"w" 以写方式打开，只能写文件， 如果文件不存在，创建该文件
                                                     如果文件已存在，先清空，再打开文件
"rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
                                                     如果文件已存在，先清空，再打开文件
"rt"   以文本读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"wt" 以文本写方式打开，只能写文件， 如果文件不存在，创建该文件
                                                     如果文件已存在，先清空，再打开文件
"rb+"   以二进制读方式打开，可以读、写文件 ， 如果文件不存在，会发生异常      
"wb+" 以二进制写方式打开，可以读、写文件， 如果文件不存在，创建该文件
                                                     如果文件已存在，先清空，再打开文件
如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾
F.truncate([size]) 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置
python  时间处理
datetime time 模块
import datetime,time
datetime.datetime.now() 返回的是字符串然后利用strftime()进行格式化为通用格式
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time.time() 返回的是时间戳 eg:1487812806.033571
time.localtime() 返回的是元组
    time.struct_time(tm_year=2017, tm_mon=2, tm_mday=23, tm_hour=9, 
    tm_min=19, tm_sec=30, tm_wday=3, tm_yday=54, tm_isdst=0)
datetime.datetime.now().date() 返回的是日期 eg:2017-02-23
timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法
获取当天的时间 datetime.datetime.now()
获取明天/前N天的时间 datetime.datetime.now() + datetime.time.delta(days=N)
获取N天前的时间 datetime.datetime.now() - datetime.time.delta(days=N)
获取当天开始和结束时间
开始时间:datetime.datetime.combine(datetime.date.today(), datetime.time.min)
结束时间:datetime.datetime.combine(datetime.date.today(), datetime.time.max)
datetime -> string datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
string -> datetime datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
datetime - > timestamp time.mktime(datetime.datetime.now().timetuple())
timestamp -> datetime datetime.datetime.fromtimestamp(1421077403.0)
strptime(string, format) 将时间字符串根据指定的格式化符转换成数组形式的时间
try except 做异常处理
1.捕获所有异常
	try:
		pass
	except Exception,e:   
    	print Exception,":",e
2.采用traceback模块查看异常
	import traceback   
	try:   
   		a=b   
    	b=c   
	except:   
    	traceback.print_exc()
3.采用sys模块回溯最后的异常
	import sys   
	try:   
 	   a=b   
	    b=c   
	except:   
	    info=sys.exc_info()   
	    print info[0],":",info[1]
4.异常写入文件中
	try:     
	    a=b     
	    b=c     
	except:     
	    f=open("c:log.txt",'a')     
	    traceback.print_exc(ffile=f)     
	    f.flush()     
	    f.close() 	    
------------------------------------------------------------------------------
幕课网学习笔记
1.如何在列表，字典，集合种筛选数据
	a.通过 for 循环迭代进行数据过滤处理
	b.通过filter() 函数过滤
		filter(lambda x: x>=0,data) //data 表示要处理的列表，返回的结果是个列表
	c.通过列表解析 字典解析处理
		[x for x in data if x >= 0]
		{x:randint(60,100) for x in xrange(1,21)} //  随机生成一个字典
		{k:v for k,v in d.iteritems() if v >= 90} //字典的解析
2.如何为元组中的元素添加命名，提高可读性
	a.通过对元组中的 index 进行定义变量，然后通过变量进行访问元组中的元素
		age,name,sex = xrange(4)
	b.利用from collections import namedtuple
		student = namedtuple('student',['name','age','sex']) //实例化
		s = student('Tom','34','men')
		访问数据，可以使用　s.name
3.统计序列中元素点出现频率
	tmp = dict.fromkeys(list,0) //建立一个默认字典，以list的值作为key,0 为字典的默认值
	利用collectios.Counter 对象进行词频的统计 
	将序列传到Counter的构造器，得到的counter 对象是元素频度的字典
	Counter.most_common(n) 得到的是频度最高的n个元素的列表
	res = Counter(data)  res.most_common(3) //获取前三个频度最高的词
4.如何更加字典中值的大小，对字典进行排序
	a.利用zip(dict.itervalues(),dict.iterkeys()) 对字典中的key,values 进行置换 然后用sorted 进行排序
	b.利用dict.items()  sorted(dict.items(),key=lambda x: x[1]) 
5.如何快速找出多个字典中的公共key
	a.利用for循环，通过判断k 是否在其它字典中进行寻找公共key
	b.利用集合set()的交 并 差进行获取
		s1.viewkeys() 得到字典s1 的key 的集合
	c.利用map和reduce进行处理
		reduce(lambda a,b:a & b,map(dict.viewkeys,[s1,s2,s3]))
6.如何让字典保持有序
	利用collections的OrderedDict 类定义一个有序的字典 d=OreredDict() d['bob'] = (1,12.34)
	保持进入字典的顺序在循环时保持不变
7.如何实现用户的历史纪录功能
	利用colletions 的deque 定义一个双向循环队列，q = deque([],5) []代表初始值，5代表队列大小
	该队列会自动移除最久的数据
	利用import pickle 进行数据的持久化到文件中 pickle.dump(list_data,open('test.log','wb')) 
	从持久化到文件中读取数据pickle.load(open('test.log'))
8.如何实现可迭代对象和迭代器对象
	可迭代对象使用内置函数iter()得到一个迭代器 iter(a)--->迭代器 a=[1,2,3,4,5,6]
	可迭代接口 a.__iter__() __getitem__() 

	iter 函数
		系统内置的iter 函数只是调用对象的__iter__方法，这个方法按照协议会返回一个迭代器，使得for循环这样的语法结构能够进行下去
		使用iter()函数转换成迭代器
	可迭代对象
		实现了__iter__ 方法，就是可以迭代的
		可以返回自身作为迭代器，也可以返回其他一个迭代器对象
		使用 For 循环的时候其实也是调用iter函数使对象返回一个迭代器，再使用迭代器进行循环
	迭代器
		python2: 实现了 next 方法
		python3: 实现了 __next__ 方法
	next 函数
		调用迭代器的 next 或__next__方法，一直到结束对象函数返回 StopIteration 异常
	迭代器和可迭代对象
		一个对象可以同时既是可迭代对象又是迭代器，只要方法里有 next(python2) 或__next__(python3) 又有 __iter__ 方法，惯用的做法是__iter__方法返回自己作为迭代器
	可以直接作用于for循环的对象统称为可迭代对象：Iterable
	可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
	可以使用isinstance()判断一个对象是否是Iterator对象
	Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看作是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
	凡是可作用于for循环的对象都是Iterable（可迭代对象）类型;
	凡是可以作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列;
	集合数据类型如 list / dict / str / 等是Iterable可迭代对象但不是Iterator迭代器，不过可以通过iter()函数可以获得一个Iterator对象。
	迭代器
		具有next方法的对象都是迭代器。在调用next方法时，迭代器会返回它的下一个值。如果next方法被调用，但迭代器没有值可以返回，就会引发一个StopIteration异常
	使用迭代器的好处：
		1.如果使用列表，计算值时会一次获取所有值，那么就会占用更多的内存。而迭代器则是一个接一个计算。
		2.使代码更通用、更简单
	什么是生成器？
		1.任何包含yield语句的函数都称为生成器。
		2.生成器都是一个迭代器，但迭代器不一定是生成器
		在函数定义中使用yield语句就创建了一个生成器函数，而不是普通的函数。
		当调用生成器函数时，每次执行到yield语句，生成器的状态将被冻结起来，并将结果返回__next__调用者。冻结意思是局部的状态都会被保存起来，包括局部变量绑定、指令指针。确保下一次调用时能从上一次的状态继续。
9.反向迭代和如何实现方向迭代
	list.reverse() 使列表反向,改变了原始列表
	reversed(list) 得到列表list的反向迭代器 使用的是__reversed__ 方法
	iter(list)	得到的是列表的正向迭代器	使用的是__iter__ 方法
10.对迭代器进行切片操作
	from itertools import islice 
	使用islice进行迭代器切片
	islice(f,100,300) 返回一个可迭代对象中的100到300行
	islice(f,500) 前500行
	islice(f,100,None) 从100行到末尾
	使用标准库中的itertools.islice() 返回的是一个迭代对象切片的生成器
11.如何在一个for 循环中迭代多个可迭代对象
	itertool.chain(list01,list02) 把对个可迭代对象串起来进行迭代
	先进行list01度迭代,然后进行list02的迭代
12.如何拆分含有多个分隔符的字符串
	1.使用split()函数，多次分隔实现多个分隔符
	2.re.split()  一次性拆分多个分隔符
	re.split(r'[;,|]*') 处理多个分隔符
13.判断字符串以a开头或结尾
	str.endswith(('.sh','.py')) 以什么结束满足一个即为true
	str.startswith(('.sh','.py')) 以什么开始满足一个即为true
14.修改文件的权限
	os.chmod('test.py',os.stat('test.py').st_mode|stat.S_IXUSR)
15.正则分组匹配
	tmp='2017-03-27'
	import re
	re.sub('(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',tmp)	利用分组然后用编号进行匹配替换
	re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<day>/\g<month>/\g<year>')
16.如何将一个小字符串拼接成大字符串
	l = ['abc',23,24,'xyz']
	s.join(iterable)  把一个可迭代对象进行拼接
	s.join(str(x) for x in l)	把整形转化为字符串进行拼接
17.如何进行字符串大左右,剧中对其
	str.ljust(with,fillchar) str.rjust() str.center()
	format(str,'<20') < 左对齐 > 右对齐 ^ 居中
18.去掉字符串中不需要的字符
	strip() lstrip() rstrip()
	replace() re.sub() 删除任意位置的字符串
	re.sub('[\r\t]','',str) 使用字符串替换删除不需要的字符
	translate() 方法删除音标等特殊字符
19.如何读写文本文件
	字符串的语义变化
	python 2.x  python 3.x
	string ---> bytes
	unicode ---> string

	python2.x 中文本文件unicode通过encode('utf8') 进行编码成string 才能写入文件中 
		文本中的string通过decode('utf8') 转换为unicode 格式才能显示
	python2.x 写入文件前对unicode进行编码,读入文件后对二进制文件进行解码
	python3.x open函数指定’t‘的文本模式,encoding指定编码格式
	f = open('pyth3.py','wt',encoding='utf8')
20.如何设置文件的缓冲区
	文件的缓冲区设置分为:全缓冲 行缓冲 无缓冲
	全缓冲 ope('filename','w',buffering=xxx) xxx默认4096 
	行缓冲 ope('filename','w',buffering=1) 遇到\n 换行符后立即写入磁盘
	无缓冲 ope('filename','w',buffering=0) 实时写入磁盘
21.如何访问文件的状态
	1.使用系统调用
		os.stat() os.lstat()-->符号链接文件的状态信息 os.fstat() -->传入的是文件的描述符
	2.使用os.path 下的一些函数
22.如何使用临时文件
	临时文件不用命名，使用后自动删除
	标准库中tempfile TemporaryFile NamedTemporaryFile 
	f=TemporaryFile() 文件系统无法查看到临时文件 ntf = NamedTemporaryFile() 生成一个临时文件，文件系统可以访问的到
23.处理csv数据
	使用标准库中的csv模块,	reader = csv.reader(file,'rb') writer = csv.writer(file,'wb') writer.writerrow(['a','b'])
24.如何读取json数据
 	json.dumps(j,seperators(',',':'))
 	json.dumps(j,sort_keys=True)  把列表数据转为json格式，并依据key排序
 	数据到json 格式 ---> json.dumps() json格式数据到python类型的数据 -->json.loads()
25.如何为创建大量实例节省内存
	定义类的__slots__属性，声明实例名字的属性
27.如何让对象支持上下文管理
	实现上下文管理协议，需要定义示例__enter__ ,__exit__方法，它们分别在with的开始和结束被调用
28.让类支持比较操作，就是对__lt__ __gt__的重写

-----------------------------------------------------------------------------------------
上下问管理器,常用在类中
__enter__():在使用with语句时调用，会话管理器在代码块开始前调用，返回值与as后的参数绑定
__exit__():会话管理器在代码块执行完成好后调用，在with语句完成时，对象销毁之前调用
__init__():构造器
在函数对象中保存着一些函数的元数据
f.__name__ 函数名
f.__doc__ 函数文档字符串
f.__moudle__ 函数所属的模块名
f.__dict__ 属性字典
f.__defaults__ 默认参数元祖
使用修饰器函数后原函数的元数据被修改了，可以利用functools 模块中的wraps进行还原@wraps(func)带参数的装饰器结果

def warn(time):
	def decorator(func):
		def wrapper(*args, **kargs):
			pass
		return wrapper
	return decorator

isinstance(value,(int,float)) 类型判断
threading.local()创建的对象中的属性，是对于每个线程独立存在的，它们相互之间无法干扰，我们称它为线程本地数据
# 使用装饰器来保存被装饰方法的元数据 @wraps(func) def wrap(*args):
属性：  公有属性  （属于类，每个类一份）  普通属性（属于对象，每个对象一份） 私有属性    （属于对象，跟普通属性相似，只是不能通过对象直接访问） 
方法：（按作用）　构造方法 析构函数
方法：（按类型）普通方法 私有方法（方法前面加两个下划线）　静态方法 类方法　属性方法
实力方法:
class Foo:
    def __init__(self, name):
        self.name = name
    def hi(self):
        print self.name
if __name__ == '__main__':
    foo01 = Foo('letian')
    foo01.hi()
Foo的type为classobj（类对象，python中定义的类本身也是对象），foo01的type为instance（实例）。
而hi()是实例方法，所以foo01.hi()会输出'letian'。实例方法的第一个参数默认为self，代指实例。
self不是一个关键字，而是约定的写法。init()是生成实例时默认调用的实例方法
实例方法就是类的实例能够使用的方法
静态方法是一种普通函数，就位于类定义的命名空间中，它不会对任何实例类型进行操作。
使用装饰器@staticmethod定义静态方法。类对象和实例都可以调用静态方法
@staticmethod
静态方法，通过类直接调用，不需要创建对象，不会隐式传递self
静态方法是不能访问实例变量和类变量的
普通的方法，可以在实例化后直接调用，并且在方法里可以通过self.调用实例变量或类变量，但静态方法是不可以访问实例变量或类变量的，一个不能访问实例变量和类变量的方法，其实相当于跟类本身已经没什么关系了，它与类唯一的关联就是需要通过类名来调用这个方法
类方法是将类本身作为对象进行操作的方法。类方法使用@classmethod装饰器定义，其第一个参数是类，约定写为cls。类对象和实例都可以调用类方法
@classmethod
类方法，方法中的self是类本身，调用方法时传的值也必须是类的公有属性
类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
就是说类方法只能操作类本身的公有字段
属性方法，属性方法的作用就是通过@property把一个方法变成一个静态属性 （类中定义）
一个静态属性了， 不是方法了， 想调用已经不需要加()号了，直接p.drive就可以了
如果我们想在属性方法里传参，比如车的品牌，我们就要用setter了，具体用法  @属性方法名.setter
用来删除属性方法，具体用法 @属性方法名.deleter
静态方法是不可以访问实例变量或类变量的
类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量
属性方法将一个方法变为类的属性，调用时不需要加()。有@property 、@属性方法名.setter、@属性方法名.deleter 三种装饰方法
class Dog(object):
    food = "gutou"
    age = "1"
    def __init__(self, name):
        self.NAME = name
    @classmethod
    def eat(self,age): #只能是类中的变量
        print(age)
        print(self.food)
    @classmethod
    def eat1(self, age):  # 只能是类中的变量
        # print(self.NAME)
        age = "2"
        self.food = "tang"
    @staticmethod
    def print_1():
        print(Dog.food, Dog.age)
	
super用来执行父类中的函数
类变量定义在类的定义之后，实例变量则是以为self.开头
class Foo(object):
    val = 0  #类变量
    def __init__(self):
        self.val = 1 实例变量
	
class Foo(object):
    val = 3
    def __init__(self):
        print self.__class__.val  ＃通过这张方式访问类变量
子类（派生类）并不会自动调用父类（基类）的init方法
class Foo2(Foo): ＃Foo为父类
    def __init__(self):
        Foo.__init__(self)   //类调用实例方法时，需要传入self指代的实例
        print self.val
	
class Foo2(Foo):
    def __init__(self):
        super(Foo2, self).__init__()  
        print self.val


