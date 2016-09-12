#-*- coding:utf8 -*-
#
#	by wangdd 2016/09/12

#利用xmltojson模块实现xml文件到json文件的转换

import xmltodict
import json

def xmltojson():
    xml = """
	<student>
	    <stid>10213</stid>
	    <info>
	        <name>name</name>
	        <mail>xxx@xxx.com</mail>
	        <sex>male</sex>
	    </info>
	    <course>
	        <name>math</name>
	        <score>90</score>
	    </course>
	    <course>
	        <name>english</name>
	        <score>88</score>
	    </course>
	</student>
	"""

    convertedDict = xmltodict.parse(xml)
    jsonStr = json.dumps(convertedDict,indent=1)
    print "jsonStr=",jsonStr

def jsontoxml():
	jsonStr ={
		"person":{
			"age":"20",
			"sex":"male",
			"info":{
				"email":"xxx@xxx.com",
				"id":"111111111"
			}
		}
	}
	convertedxml = xmltodict.unparse(jsonStr)
	print convertedxml


