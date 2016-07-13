#!/usr/bin/python
#coding=utf-8

#	by wangdd 2016/03/30

#fabric 是基于python实现的ssh命令行工具，可以实现本地或远程shell命令，文件的上传，下载等
#安装 pip install fabric

# fab -H 192.168.1.200 -f python_fabric.py host_type
#fab 引用默认文件名fabfile.py ,可以通过使用 -f 参数指定相应的文件
#fab 常用参数
# -l 显示定义好的任务函数名;-f 指定fab入口文件，默认fabfile.py;-g 指定中转设备，例如堡垒机;-H 指定目标主机
#-P 以异步并行方式运行多主机任务，默认串行执行
#-R 以角色名区分不同业务组设备; -t 设备连接超时时间;-T设置远程主机命令超时时间; -w 执行命令失败，发告警，而非默认中止

#fabfile的编写
#evn对象的作用是定义fabfile的全局设定
#env.hosts 定义目标主机 env.exclude.hosts 排除指定主机 env.user 定义用户名 env.port 定义目标主机端口
#env.password 定义密码 
#env.passwords 与password功能一样，区别在于不同主机不同密码的应用，配置passwords时需配置用户,主机,端口等信息
#env.passwords = {'root@1.1.1.1':'111111','root@2.2.2.2':'22222'}
#env.gateway 定义网关
#env.deploy_release_dir 自定义全局变量，格式env.+'变量名' env.age 
#env.roledefs 定义角色分组,比如web和db组
#env.roledefs = {'webs':['1.1.1.1','2.2.2.2'],'dbs':['3.3.3.3','4.4.4.4']}
# @roles('webs')
# def webtask():
#	run('hostname')

#常用api
#local,执行本地命令	lcd 切换本地目录	cd 切换远程目录		run 执行远程命令	sudo sudo方式执行远程命令
#put 上传本地文件到远程主机	get 从远处主机下载文件到本地  prompt 获取用户输入信息	confirm		获取提示信息确认
#reboot 重启远程主机 @task 函数修饰符标识入口函数，标识的函数为fab可调用的
#@runs_once	函数修饰符，标识的函数只会执行一次，不受多台主机影响

from fabric.api import *

env.user = 'wangdd'
env.hosts = ['192.168.1.201']
env.password = '123456'

def host_type():
	run('uname -a')
@runs_once	#查看本地系统信息，当有多台主机时只运行一次
def local_task():
	local('hostname')

def remote_task():
	with cd('/usr/local/src'):	#with 的作用是让后面的表达式的语句继承当前状态，实现'cd /usr/local/src && ls -l' 的效果
		run('ls -l')

#动态获取远程主机的目录列表
@runs_once	#远程主机遍历过程中，只有第一台触发此函数
def input_raw():
	return prompt('Please input directory name:',default='/home')

def worktask(dirname):
	run('ls -l '+dirname)

@task #限定此下面的函数对fab命令可见,通过-l 命令可以看到的函数
def get_dirname_main():
	getdirname	= input_raw()
	worktask(getdirname)

#网关模式文件上传和执行
from fabric.context_managers import *
from fabric.contrib.console import confirm

env.gateway = '192.168.1.200'	#定义堡垒机

lpackpath = "/usr/local/src/soft/ifstat-1.1.tar.gz"	#本地安装包路径
rpackpath = "/tmp/install"	#定义远程安装包路径


@runs_once
def tar_task():	#本地打包任务函数
	with('/var/log/'):
		local('tar -czf test.tar.gz messages')

@task
def put_task():	#上传文件函数
	run('mkdir -p /tmp/install')
	with settings(warn_only=True):	#上传过程中出现异常时继续执行，非中止
		result = put( lpackpath,rpackpath)	#上传安装包
	if result.failed and not confirm('put file failed,Continue[Y/N]?'):
		abort("Aborting file put task!")	#出现异常时，确认用户是否继续

@task
def check_task():	#校验文件函数
	with settings(warn_only=True):
		#本地local命令配置capture=Ture才能捕获返回值
		lmd5=local('md5sum file.tar.gz',capture=True).split(' ')[0]
		rmd5=run('md5sum file.tar.gz').split(' ')[0]	#split()依据某个元素进行分割，类似awk 中的-F 
	if lmd5==rmd5:
		print "OK"
	else:
		print "Error"

def run_task():	#执行远程命令,安装lnmp环境
	with cd('/tmp/install'):
		run('tar zxvf ifstat-1.1.tar.gz')
		with cd('ifstat-1.1/'):
			run('./configure')
			run('make && make install')

@task
def put_file_main():
	put_task()
	#run_task()

#通过env.roledefs实现不同的角色，部署不同的业务应用
#新增一个模块
from fabric.colors import *

env.roledefs = {
	'webserver':['192.168.1.200'],
	'dbserver':['192.168.1.201']
}

env.passwords = {
	'wangdd@192.192.168.1.200':'123456',
	'wangdd@192.168.1.201':'123456'
}

@roles('webserver')		#webtask 任务函数引用webserver角色
def webtask():	#部署nginx
	print yellow('Install nginx php php-fpm...')
	with settings(warn_only=True):
		run('yum -y install nginx')
		run('yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd')
		run('chkconfig --levels 235 php-fpm on')
		run('chkconfig --levels 235 nginx on')

@roles('dbserver')	#dbtask任务函数引用dbserver角色
def dbtask():	#安装数据库
	print yellow('Install Mysql...')
	with settings(warn_only=True):
		run('yum -y install mysql mysql-server')
		run('chkconfig --levels 235 mysqld on')

@roles('webserver','dbserver')	#publictask 任务函数引用两角色
def publictask():
	print yellow('Install epel ntp ...')
	with settings(warn_only=True):
		run('rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
		run('yum -y install ntp')



def deploy():
	execute(publictask)
	execute(webtask)
	execute(dbtask)