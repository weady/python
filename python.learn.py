#!/usr/bin/python
#coding=utf8

import subprocess
#command 1
cmd = "ls -l"
subprocess.call(cmd,shell=True)
#command 2
command = "df"
command_args = "-lh"
subprocess.call([command,command_args])
