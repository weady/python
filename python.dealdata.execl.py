#!/usr/bin/python
#coding:utf-8
#
#	by wangdd 2016/07/06 

import re
import sys
import xlsxwriter
import threading
import time
reload(sys)
sys.setdefaultencoding('utf8')

data_list = []
list_lock = threading.Lock()
row = 1
col = 0

line_re = re.compile(r'''.*<id>(?P<id>\d+)</id>
			<name><!\[(?P<name>.*)\]></name>
			<englishName>(?P<englishName>.*)</englishName>
			<programClass><!\[(?P<programClass>.*)\]></programClass>
			<programType><!\[(?P<programType>.*)\]></programType>
			<desc><!\[(?P<desc>.*)\]></desc>
			<premiereDate>(?P<premiereDate>.*)</premiereDate>
			<definition><!\[(?P<definition>.*)\]></definition>
			<smallPoster><!\[(?P<smallPoster>.*)\]></smallPoster>
			<poster><!\[(?P<poster>.*)\]></poster>
			<bigPoster><(?P<bigPoster>.*)></bigPoster>
			<tag><!\[(?P<tag>.*)\]></tag>
			<director><!\[(?P<director>.*)\]></director>
			<leadingRole><!\[(?P<leadingRole>.*)\]></leadingRole>
			<scriptWriter>(?P<scriptWriter>.*)</scriptWriter>
			<years><!\[(?P<years>.*)\]></years>
			<zone><!\[(?P<zone>.*)\]></zone>
			<copyright><!\[(?P<copyright>.*)\]></copyright>
			<cpCode><!\[(?P<cpCode>.*)\]></cpCode>
			<cpCodeSourceId><!\[(?P<cpCodeSourceId>.*)\]></cpCodeSourceId>
			<cpCodeProgramName><!\[(?P<cpCodeProgramName>.*)\]></cpCodeProgramName>
			<price>(?P<price>.*)</price>
			<updateTime>(?P<updateTime>.*)</updateTime>
			<programTotalCount>(?P<programTotalCount>.*)</programTotalCount>
			<programs>(?P<programs>.*)</programs>
			.*
				''',re.X)

def task(line):
    global workbook
    global worksheet
    global row
    global col
    m = line_re.search(line.encode('utf8').strip())
    if m:
	groupdict = m.groupdict()
	worksheet.write(row, col ,groupdict['id'])
	worksheet.write(row, col+1 ,groupdict['name'])
	worksheet.write(row, col+2 ,groupdict['englishName'])
	worksheet.write(row, col+3 ,groupdict['programClass'])
	worksheet.write(row, col+4 ,groupdict['programType'])
	worksheet.write(row, col+5 ,groupdict['desc'])
	worksheet.write(row, col+6 ,groupdict['premiereDate'])
	worksheet.write(row, col+7 ,groupdict['definition'])
	worksheet.write(row, col+8 ,groupdict['smallPoster'])
	worksheet.write(row, col+9 ,groupdict['poster'])
	worksheet.write(row, col+10 ,groupdict['bigPoster'])
	worksheet.write(row, col+11 ,groupdict['tag'])
	worksheet.write(row, col+12 ,groupdict['director'])
	worksheet.write(row, col+13 ,groupdict['leadingRole'])
	worksheet.write(row, col+14 ,groupdict['scriptWriter'])
	worksheet.write(row, col+15 ,groupdict['years'])
	worksheet.write(row, col+16 ,groupdict['zone'])
	worksheet.write(row, col+17 ,groupdict['copyright'])
	worksheet.write(row, col+18 ,groupdict['cpCode'])
	worksheet.write(row, col+19 ,groupdict['cpCodeSourceId'])
	worksheet.write(row, col+20 ,groupdict['cpCodeProgramName'])
	worksheet.write(row, col+21 ,groupdict['price'])
	worksheet.write(row, col+22 ,groupdict['updateTime'])
	worksheet.write(row, col+23 ,groupdict['programTotalCount'])
	row+=1
	col=0
	
def work(index):
    global data_list
    global list_lock
    while True:
        time.sleep(0.3)
        if len(data_list) > 0:
            list_lock.acquire()
            line_data = data_list.pop(0)
            list_lock.release()
            task(line_data)
        else:
            break


def start_work():
    global data_list
    global workbook
    global worksheet
    global row
    global col
    workbook = xlsxwriter.Workbook("test.xlsx")
	
    worksheet = workbook.add_worksheet()

    format_title = workbook.add_format()
    format_title.set_border(1)
    format_title.set_bg_color('#cccccc')
    format_title.set_align('center')
    format_title.set_bold()

    title = ['id','name','englishName','programClass','programType','desc','premiereDate','definition','smallPoster','poster','bigPoster','tag','director','leadingRole','scriptWriter','years','zone','copyright','cpCode','cpCodeSourceId','cpCodeProgramName','price','updateTime','programTotalCount']
    #worksheet.write 方法将数据写入 xlsx 表格中
    #参数依次为：行号、列号、数据、[格式]           
    worksheet.write_row('A1',title,format_title)
    file_data = open(u'dong.xml', 'r')
    data_list = list(file_data.readlines())
    work_threads = []
    for index in range(0,100):
        th = threading.Thread(target=work, args=(index,))
    	work_threads.append(th)
    for th in work_threads:
    	th.start()

    for th in work_threads:
        threading.Thread.join(th)

   	#显式关闭workbook，若不显式指定，则作用域结束后自动关闭\
    file_data.close()
    workbook.close()


start_work()
