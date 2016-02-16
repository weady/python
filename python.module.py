#!/usr/bin/python
# coding:utf-8
#
#	by wangdd 2016/02/02
#

import subprocess


#subprocess 模块可以用于执行shell命令
def sub_mode():
    #command 1
    uname = "uname"
    uname_args = "-a"
    subprocess.call([uname,uname_args])
    print ""
    #command 2
    diskspace = "df -lh"
    subprocess.call(diskspace,shell=True)

sub_mode()
