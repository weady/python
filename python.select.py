#!/usr/bin/env python
#coding: utf-8
#

import os
import cPickle

def menu():
    '''设置menu目录,提供给用户的操作接口'''
    print '''
	1.add user info
	2.display all user info
	3.update user info by username
	4.del user by username
	5.sort user info
	0.exit
    '''
    op = raw_input('请输入你的选择:')
    return op

def txl_exit():
    '''退出程序'''
    os._exit(0)

def txl_error():
    '''当用户输入选项不在选项范围内时报错'''
    print
    print '非法选项,请重新输入!'

def txl_add():
    '''添加用户'''
    name = raw_input('名字:')
    age = raw_input('年龄:')
    gender = raw_input('性别:')
    tel = raw_input('手机号:')
    txl.append({'name':name,'age':age,'gender':gender,'tel':tel})
    txl_save()

def txl_display():
    '''显示用户信息'''
    txl_load()
    print
    if len(txl) >0:
	print "姓名\t年龄\t性别\t手机号"
	print "-------------------------------"
	for x in txl:
		print '%(name)s\t%(age)s\t%(gender)s\t%(tel)s' % x
	print "-------------------------------"
    else:
	print 
	print "This is a empty file,no info!"

def txl_save():
    '''使用cpickle进行列表到字符串的转换 然后写入文件'''
    s = cPickle.dumps(txl)
    fp = file(fname,'w')
    fp.write(s)
    fp.close()

def txl_load():
    '''从文件读取信息,然后使用cPickle进行字符串到列表的转换'''
    del txl[:]
    if os.path.exists(fname):
	fp = file(fname)
	s = fp.read()
	fp.close()
	txl.extend(cPickle.loads(s))

def txl_del():
    '''根据用户名删除信息'''
    name = raw_input('输入要删除的用户名:')
    for line in txl:
	try:
		if line['name'] == name:
			txl.remove(line)
			print "删除用户%s成功" % name
			break
	except:
		print "删除失败"
    txl_save()

def txl_sort():
    '''根据用户输入数据进行排序'''
    op = raw_input('Order By [name|age|gender|tel]')
    txl.sort(key= lambda x: x[op])
    txl_display()

def txl_update(status=True):
    '''根据用户进行数据的更新,用户名不可变'''
    txl_display()
    name = raw_input('输入要修改的用户名:')
    for line in txl:
	if line['name'] ==name:
		status=False
		old_age = line['age']
		old_gender = line['gender']
		old_tel = line['tel']
		age = raw_input('年龄:')
		gender = raw_input('性别:')
		tel = raw_input('电话:')
		if len(age) == 0:
			line['age'] = old_age
		else:
			line['age'] = age
		if len(gender) == 0:
			line['gender'] = old_gender
		else:
			line['gender'] = gender
		if len(tel) == 0:
			line['tel'] = old_tel
		else:
			line['tel'] = tel
		break
    if status:
	print "无此用户"
    txl_save()


def main():
    '''主程序'''
    while True:
	op = menu()
	ops.get(op,txl_error)()

#定义数据
fname = 'contact.db'

txl = []

ops = {
    '1':txl_add,
    '2':txl_display,
    '3':txl_update,
    '4':txl_del,
    '5':txl_sort,
    '0':txl_exit,
}

#程序入口
if __name__ == '__main__':
    main()

