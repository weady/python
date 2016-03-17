#coding=utf-8

#	by wangdd 2016/03/12

#python-rrdtool模块进行画图
#常用方法:create update graph fetch 
#1.create 创建一个后缀是rrd的rrdtool数据库
#2.update 存储一个新值到rrdtool数据库,updatev 和update类似，区别是每次插入都会
		  #返回一个状态码,updatev 用0表示成功，-1 表示失败
#3.graph 用于画图
#4.fetch 数据库进行查询

#rrd创建到输出图像的过程:create rrd----update rrd(graph png)----query rrd
import rrdtool
import time,psutil

#创建rrd数据库
def create():
	cur_time = str(int(time.time()))

	#数据写频率 --step 300秒，5分钟一个数据点
	rrd = rrdtool.create('Flow.rrd','--step','300','--start',cur_time,
			#定义数据源eth0_in,eth0_out，类型counter递增，600s没收到数据，用unknown代替，0最小U代表最大值不确定
			'DS:eth0_in:COUNTER:600:0:U','DS:eth0_out:COUNTER:600:0:U',	
			#RRA用于指定数据如何存放,我们可以把以恶RRA看成一个表,RRA:CF:xff:steps:rows
			'RRA:AVERAGE:0.5:1:600',	#每隔5分钟(1*300秒)存一次数据的平均值，存600笔，2天
			'RRA:AVERAGE:0.5:6:700',	#每隔30分钟(6*300秒)存一次数据的平均值，存700笔，2周
			'RRA:AVERAGE:0.5:24:755',	#每隔2小时(24*300秒)存一次数据的平均值，存755笔，2月
			'RRA:AVERAGE:0.5:288:797',	#每隔24小时(288*300秒)存一次数据的平均值，存797笔，2年
			'RRA:MAX:0.5:1:600',
			'RRA:MAX:0.5:6:700',
			'RRA:MAX:0.5:24:755',
			'RRA:MAX:0.5:288:797',
			'RRA:MIN:0.5:1:600',
			'RRA:MIN:0.5:6:700',
			'RRA:MIN:0.5:24:755',
			'RRA:MIN:0.5:288:797')
	if rrd:
		print rrdtool.error()

def update_rrd():

	total_in = psutil.net_io_counters()[1]
	total_out = psutil.net_io_counters()[0]	
	starttime = int(time.time())
	update = rrdtool.updatev('/usr/local/src/Flow.rrd','%s:%s:%s')	% (str(starttime),str(total_in),str(total_out))

	print update

def graph():
	title = "Server Network traffic flow ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"
	#"--x-grid,"MINUTE:12:HOUR:1:HOUR:1:0:%H";
	#"MINUTE:12"	控制每隔12分钟放置一根次要格线
	#"HOUR:1"	每隔1小时放置一根主要格线
	#"HOUR:1"	每隔1小时输出一个label标签
	#"0:%H"		0表示数字对齐格线，%H表示标签以小时显示

	rrdtool.graph( "Flow.png", "--start", "-1d","--vertical-label=Bytes/s","--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H",\
	 "--width","650","--height","230","--title",title,
	 "DEF:inoctets=Flow.rrd:eth0_in:AVERAGE",	#指定网卡入流量数据源DS及CF
	 "DEF:outoctets=Flow.rrd:eth0_out:AVERAGE",	
	 "CDEF:total=inoctets,outoctets,+",	#通过CDEF合并网卡出入流量，得出总流量total
	 "LINE1:total#FF8833:Total traffic",
	 "AREA:inoctets#00FF00:In traffic",
	 "LINE1:outoctets#0000FF:Out traffic",	
	 "HRULE:6144#FF0000:Alarm value\\r",	#绘制水平线,作为告诫线,阈值6.1K
	 "CDEF:inbits=inoctets,8,*",	#将入流量换算成bit，即*8，计算结果给inbits
	 "CDEF:outbits=outoctets,8,*",
	 "COMMENT:\\r",
	 "COMMENT:\\r",
	 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",		#绘制入流量的平均值
	 "COMMENT:   ",	
	 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",
	 "COMMENT:  ",
	 "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",
	 "COMMENT: ",
	 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
	 "COMMENT: ",
	 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",
	 "COMMENT: ",
	 "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")
