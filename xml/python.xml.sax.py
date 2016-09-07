#-*- coding:utf8 -*-
#
#	by wangdd 2016/09/08

# 利用xml.sax处理xml文件需要重写startElement(),endElement(),characters()三个方法

import xml.sax


class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = "" #保存当前处理的标签
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # 元素开始事件处理,tag表示标签的名字,attributes表示标签的属性
   def startElement(self, tag, attributes):

      self.CurrentData = tag
      if tag == "movie":
         print "*****Movie*****"
         title = attributes["title"]
         print "Title:", title

   # 元素结束事件处理
   def endElement(self, tag):
      if self.CurrentData == "type":
         print "Type:", self.type
      elif self.CurrentData == "format":
         print "Format:", self.format
      elif self.CurrentData == "year":
         print "Year:", self.year
      elif self.CurrentData == "rating":
         print "Rating:", self.rating
      elif self.CurrentData == "stars":
         print "Stars:", self.stars
      elif self.CurrentData == "description":
         print "Description:", self.description
      self.CurrentData = "" #当前标签处理完毕后,把CurrentData进行置空为下一个标签使用

   # 内容事件处理,就是对标签的文本进行处理,content表示标签内的文件内容
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content 
  
if ( __name__ == "__main__"):
   
   # 创建一个 XMLReader,创建一个解析器
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # 重写 ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse("test.xml")