#!/usr/bin/python
#-*-coding:utf8-*-
#
#	by wangdd 2016/09/08
#

#DOM 文档对象模型,一个 DOM 的解析器在解析一个 XML 文档时
#一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里
#之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件

from xml.dom.minidom import parse
from xml.dom import minidom
import xml.dom.minidom

#--------------------读XML文件---------------------------
def readxml01(file):
	# 使用minidom解析器打开 XML 文档
	DOMTree = xml.dom.minidom.parse(file)
	collection = DOMTree.documentElement
	if collection.hasAttribute("shelf"):
	   print "Root element : %s" % collection.getAttribute("shelf")

	# 在集合中获取所有电影
	movies = collection.getElementsByTagName("movie")

	# 打印每部电影的详细信息
	for movie in movies:
	   print "*****Movie*****"
	   if movie.hasAttribute("title"):
	      print "Title: %s" % movie.getAttribute("title")

	   type = movie.getElementsByTagName('type')[0]
	   print "Type: %s" % type.childNodes[0].data
	   format = movie.getElementsByTagName('format')[0]
	   print "Format: %s" % format.childNodes[0].data
	   rating = movie.getElementsByTagName('rating')[0]
	   print "Rating: %s" % rating.childNodes[0].data
	   description = movie.getElementsByTagName('description')[0]
	   print "Description: %s" % description.childNodes[0].data

def readxml02(file):
	dom = minidom.parse(file)#用minidom的解析器打开文件

	root  = dom.documentElement#得到了xml文档的根节点

	people = root.getElementsByTagName("people")
	#所有的people节点集合
	#getElementsByTagName  复数 
	people1 = people[0]
	people2 = people[1]

	age = people1.getElementsByTagName("age")
	#集合 [age]
	#print(people1.nodeName,people1.firstChild.nodeValue,people1.getAttribute("name"))
	#print(age[0].childNodes[0].nodeValue)
	print(age[0].firstChild.nodeValue)

	#firstChild == childNodes[0]

#--------------------写XML文件---------------------------
	'''
	doc.createElement(Node name) 生成XML节点
	node.setAttribute(att name,att value) 给结点添加属性值
	doc.createTextNode(text) 节点的内容
	node.appendChild(Node name) 添加到指定的节点下面
	xmlfile.write(doc.toprettyxml()) 把内存中的xml写入到文件中
	'''

doc = minidom.Document()
person = doc.createElement("person")
doc.appendChild(person)
#创建了一个根节点
def addNode(node_dict):#希望用户输入一个字典,来创建节点
	people = doc.createElement("people")
	people.setAttribute("name",node_dict["name"])

	age = doc.createElement("age")
	age_text = doc.createTextNode(node_dict["age"])
	#创建一个文本节点值
	age.appendChild(age_text)
	#给age这个节点添加了文本内容
	people.appendChild(age)

	sex = doc.createElement("sex")
	sex_text = doc.createTextNode(node_dict["sex"])
	#创建一个文本节点
	sex.appendChild(sex_text)
	people.appendChild(sex)

	salary = doc.createElement("salary")
	salary_text = doc.createTextNode(node_dict["salary"])
	#创建一个文本节点
	salary.appendChild(salary_text)
	people.appendChild(salary)
	person.appendChild(people) #最后把所有内容添加的根节点下
#makefile 一次编写 终生受益
user_info = {"name":"Jack","age":"16","sex":"male","salary":"1000"}
user_info1 = {"name":"Bob","age":"20","sex":"female","salary":"34000"}
addNode(user_info)
addNode(user_info1)
xmlfile = open("minidom.xml",'w')

xmlfile.write(doc.toprettyxml()) #把内存中配置好的信息写入到磁盘的文件中
xmlfile.close()