#-*- coding:utf-8 -*-
#
#	by wangdd 2016/06/01	
#
#网络爬虫的基本模块urllib

import urllib
import chardet #字符集检测模块
import urllib2
import random
"""
		getcode()	获取状态码
		geturl()	获取输入的url
		getinfo()	获取头部信息
		read()		读取网页内容
		urllib.open(url)	查看一个网站的内容
		urllib.urlretrieve(url,'/tmp/test.html',function)    把一个网页的内容保存到本地文件中
			function 为回调函数，必须为三个参数
			1.目前为止传递的数据块数量
			2.每个数据库的大小，单位byte
			3.远程文件的大小
"""
url = 'http://www.163.com/'

#-----------------------------------------------------------------------------
def base_urllib():
	html = urllib.urlopen(url)
	info = urllib.urlopen(url).info()
	print html.geturl()
	print html.read()
	print dir(info)	#打印该类的方法
	print info.getparam('charset')	#获取网页编码
	html.close
#-----------------------------------------------------------------------------
def callback(a,b,c):
	download_process = 100*a*b/c
	if download_process > 100:
		download_process = 100
	print '%.2f%%' % download_process+'\r'

	urllib.urlretrieve(url,'web.html',callback)
#-----------------------------------------------------------------------------
def auto_detect(url):
	content = urllib.urlopen(url).read()
	print url,chardet.detect(content)	#检测出页面的编码格式
#-----------------------------------------------------------------------------
my_headers=[
	"Mozilla/5.0 (X11;Ubuntu;Linux i686;rv:10.0) Gecko/20100101 Firefox/10.0"
]
get_url = 'http://news.163.com/16/0529/20/BO8SVPJ200011229.html'
def get_content(url,headers):
	"""
	@利用爬虫获取403状态的页面信息
	"""
	random_header = random.choice(headers)
	req = urllib2.Request(url)
	req.add_header('User-Agent',random_header)
	req.add_header('Host','news.163.com')
	req.add_header('Referer','http://news.163.com/')
	req.add_header('GET',url)
	#添加的头部信息可能有问题
	content = urllib2.urlopen(req).read()
	return content
	
print get_content(get_url,my_headers)
#-----------------------------------------------------------------------------
#注释:结合代理ip和伪装头部信息可以使用更强大的网络爬虫功能








