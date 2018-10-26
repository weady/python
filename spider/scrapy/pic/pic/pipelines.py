# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib2
import sys
import re
import os

reload(sys)
sys.setdefaultencoding("utf-8")

class PicPipeline(object):
    def process_item(self, item, spider):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
        url = item['addr']
        req = urllib2.Request(url)
        req.add_header('User-Agent', user_agent)
        res = urllib2.urlopen(req)
        name = item['name']
        file_name = os.path.join(r'E:\down_pic', name + '.jpg')
        with open(file_name, 'wb') as fp:
            fp.write(res.read())
