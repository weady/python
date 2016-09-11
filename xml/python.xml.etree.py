#!/usr/bin/python
#coding:utf8

#利用xml.etree.ElementTree操作xml文件

import xml.etree.ElementTree as ET

def readxml():
	tree = ET.parse('test.xml')
	root = tree.getroot()
	#我们获取到了根节点
	print(root.tag) #获取根标签的名字
	print root.attrib['name'] #获取根标签的属性名
	perplelist = root.iter("people") #获取根标签下所有的people标签



	for people in root.findall("people"): #root.findall() = root.iter()
		print("-----------------")
		# print(people.attrib) 获取标签的属性
		print("name:",people.get("name"))

		age = people.find("age") #定位到某个标签
		sex = people.find("sex")
		salary = people.find("salary")

		print("age:",age.text)	#获取标签的值
		print("sex:",sex.text)
		print("salary:",salary.text)

def write():
	xmltree =  ET.ElementTree() #在内存中创建一个xmltree
	person = ET.Element("person") #生成根节点
	#ctrl+shift+b
	xmltree._setroot(person)
	#在xml对象中设置了根节点
	people = ET.SubElement(person,'people',{"name":"Jack"})
	#SubElement 创建子节点 然后把节点名称和属性 在函数参数的第二个和第三个部分写到
	age = ET.Element("age") #利用ET.Element() 在people子节点下创建相应的子节点
	age.text = "18"	#为字节点赋值
	people.append(age) #把子节点添加到people父节点中
	sex = ET.Element("sex")
	sex.text = "male"
	people.append(sex)
	salary = ET.Element("salary")
	salary.text = "30000"
	people.append(salary)

	ET.dump(indent(person))
	xmltree.write("write.xml")

def indent(elem,level=0): #美化输出函数
	i = "\n" + level*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
		#strip去除在文本节点前和文本节点后的空格
			elem.text = i + "  "
		for e in elem:
			indent(e,level+1)
		if not e.tail or not e.tail.strip():
			e.tail = i 
	if level and (not elem.tail or not elem.tail.strip()):
		elem.tail = i
	return elem


write()
