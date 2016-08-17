#-*-coding:utf8-*-

#利用xml.sax模块进行xml文件的处理,需要重写startElement(),characters(),endElement()三个方法

import xml.sax
class peoplexml(xml.sax.ContentHandler):
	def __init__(self):#构造器
		self.currentData = ""#存储当前获取到的标签
		self.age=""
		self.sex=""
		self.salary=""
	def startElement(self,tag,attributes):
		self.currentData = tag#把我们当前处理的标签保存下来
		#处理开始标签，tag标签,attributes属性,
		if tag == "people":#如果标签是people 我们要获取他的属性值
			print('--------------')#华丽的分割线
			name = attributes["name"]
			#通过标签属性 来获取到属性对应的值
			print('name:',name)
	def characters(self,content): #在遇到文本的时候 做这个函数
		if self.currentData=='age':#如果标签等于age
			self.age=content
		elif self.currentData =='sex':#如果标签等于sex
			self.sex=content
		elif self.currentData == "salary":#如果标签等于salary
			self.salary=content#我们标签里的值保存到我们类中的数据对象中
	def endElement(self,tag):#遇到闭合标签的时候 来做这个函数
		if self.currentData == "age":
			print("age:",self.age)
		elif self.currentData == "sex":
			print("sex:",self.sex)
		elif self.currentData == "salary":
			print("salary:",self.salary)
		self.currentData=""#处理完标签之后，我们把这个self.currentData初始化成空串
myparser = xml.sax.make_parser()
#创建了一个xml解析器
handler = peoplexml()
#初始化我们自己继承ContentHandler的重写的子类
myparser.setContentHandler(handler)
myparser.parse('read.xml')