#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Document: Remove Synctoycmd sync expired .tmp files"""

import os
import time
import datetime
import re

def fileremove(filename, timedifference):
    '''remove file'''

    date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
    print date

    now = datetime.datetime.now()
    print now

    print 'seconds difference: %d' % ((now - date).seconds)

    if (now - date).seconds > timedifference:
        if os.path.exists(filename):
            #os.remove(filename)
            print 'remove file: %s' % filename
        else:
            print 'no such file: %s' % filename


#包含今天,保留两天的日志文件,日志文件格式xxxx.2017-11-10.log
def del_file(days):
	path= os.getcwd()
	files = os.listdir(path)
	two_days_ago = datetime.date.today() - datetime.timedelta(days=days)
	two_days_ago_stamp = time.mktime(time.strptime(str(two_days_ago), "%Y-%m-%d"))
	for line in files:
		if 'rsync_log_file' in line:
			time_tag = line.split('.')[1]
			time_tag_stamp = time.mktime(time.strptime(time_tag, "%Y-%m-%d"))
			if two_days_ago_stamp >= time_tag_stamp:
				print line

del_file(3)
