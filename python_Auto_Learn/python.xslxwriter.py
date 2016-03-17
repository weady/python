#coding=utf-8

#	by wangdd 2016/03/10


#python 操作excel 的模块xlsxwriter模块

#workbook类的主要方法
#1.add_worksheet()	创建一个工作表
#2.add_format()	定义一个新的格式对象用于格式化单元格
#3.add_chart()	创建一个图标对象

#worksheet类的主要方法
#1.write('row','col','值')
#2.set_row('row','height','format','option')
#3.set_column()
#4.insert_image('row','col','image','option')

#chart类
#通过workbook.add_chart() 方法创建，再通过worksheet.insert_chart('B3','chartname')


import xlsxwriter

def excel():
	workbook = xlsxwriter.Workbook('test.xlsx')	#创建一个excel文件
	worksheet = workbook.add_worksheet()	#创建一个工作表对象
	worksheet1 = workbook.add_worksheet('name')	#创建第二个工作表对象
	#chart = workbook.add_chart({'type':'line'})	#创建一个线条类型的图标对象
	#

	worksheet.set_column('A:A',20)	#设定第一列宽度为20像素
	bold = workbook.add_format({'bold':True})	#定义一个加粗的格式对象

	worksheet1.write('A1',u'第二个工作表')
	worksheet.write('A1','test')
	worksheet.write('A2','wangdong',bold)	#A2单元格对象加粗
	worksheet.write('B2',u'王东',bold)

	worksheet.write(2,0,333)	#2代表第三行，0代表第一列
	worksheet.write(3,0,100)
	worksheet.write(4,0,'=SUM(A3:A4)') # 求 A3:A4的和,结果写入A5

	worksheet.insert_image('B5','test.jpg',{'url':'http://www.baidu.com'})	#插入图片
	workbook.close()

def excel_report():
	workbook = xlsxwriter.Workbook('chart.xlsx')	#创建一个Excel文件
	worksheet = workbook.add_worksheet()	#创建一个工作表单
	chart = workbook.add_chart({'type':'column'})	#创建一个柱型图表对象

	#定义表头数据
	title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六',u'星期日',u'平均流量']
	#定义频道名称
	buname =[u'官网',u'BBS',u'Blog',u'BOSS',u'邮件系统']

	data = [
		[111,214,134,62,644,39,123],
		[11,14,134,632,64,389,13],
		[91,214,14,632,644,39,23],
		[111,24,34,63,644,89,123],
		[101,214,134,632,44,389,83],
	]

	format = workbook.add_format()
	format.set_border(1)
	format.set_align('center')

	format_title = workbook.add_format()
	format_title.set_border(1)
	format_title.set_bg_color('#cccccc')
	format_title.set_align('center')
	format_title.set_bold()

	format_avg = workbook.add_format()
	format_avg.set_border(1)
	format_avg.set_bg_color('#FF0000')
	format_avg.set_num_format('0.00')

	#填充数据
	worksheet.write_row('A1',title,format_title)	#数据按行填充
	worksheet.write_column('A2',buname,format_title)	#数据按列填充
	worksheet.write_row('B2',data[0],format)
	worksheet.write_row('B3',data[1],format)
	worksheet.write_row('B4',data[2],format)
	worksheet.write_row('B5',data[3],format)
	worksheet.write_row('B6',data[4],format)

	#定义图表数据
	def chart_series(cur_row):
		worksheet.write_formula('I'+cur_row,'=AVERAGE(B'+cur_row+':H'+cur_row+')',format_avg)

		chart.add_series({
			'categories':'=Sheet1!$B$1:$H$1',	#categories 用于设置图表类别标签范围，X轴
			'values':'=Sheet1!$B$'+cur_row+':$H$'+cur_row,	#一周所有的数据作为数据区域
			'line':{'color':'black'},
			'name':'=Sheet1!$A$'+cur_row,
			})

	for row in range(2,7):
		chart_series(str(row))

	#chart.set_table()
	#chart.set_style(30)
	chart.set_size({'width':577,'height':287})	#图表大小
	chart.set_title({'name':u'业务流量周报表'})	#表头
	chart.set_y_axis({'name':'Mb/s'})	#Y轴

	worksheet.insert_chart('A8',chart)

	workbook.close()



excel_report()












