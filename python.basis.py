#!/usr/bin/python
#coding: utf-8
#
# by wangdd 2015/12/4

import re
import time;
import calendar;
test = time.localtime(time.time())
test02 = time.asctime( time.localtime(time.time()) )
print test
print test02
cal = calendar.month(2015,11)
print cal

print "Hello world!!"
#raw_input("Press any key to exit.")
import sys;x = 'foo';sys.stdout.write(x + '\n')
a = 23
b = 10
c = a - b
print "value is c",c
if ( a >b ):
	print "a gt b"
else:
	print "a lt b"
if not( a and b ):
   print "Line 5 - a and b are true"
else:
   print "Line 5 - Either a is not true or b is not true"
if ( b == 10 ) :
	print "OK,The Number is ",a
else:
	print "Error"
name = 'wangdong'
if name == 'wangdong':
	print 'name is',name
else:
	print 'name is null'
while b <15:
	print b,'is less than 15'
	b+=1
else:
	print b,'is more then 15'
	print 'Good bye!'
for var in 'ABCD':
	print var

fruits = ['banana', 'apple',  'mango']
for list in fruits:
	if list=='banana':
		pass
		print "test"
	print list

print '----------'
print fruits[1]
print '----------'
fruits.append('test')
print fruits[3]

print r'\n Good bye!!'

print "my name is %s ,age is %d" % ('wangdong',28)
# raw_input 从标准输入读取
#str = raw_input("Enter one number:");
#print "your enter number is:",str
#---------------------------------------------------
#re.sub 替换命令
num = "12345 $number"
phone = re.sub(r'\$.*$','',num)
print "number is :",phone

#re.match
line = "who are you?"
match = re.match(r'who',line,re.M|re.I)
search = re.search(r'you\?',line,re.M|re.I)
#if 多条件用 or and 或 a in list,a not in list
if match and search :
	print "匹配成功 match:",match.group()
	print "匹配成功 search:",search.group()
else:
	print "匹配失败 not match"
