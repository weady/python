#!/bin/bash
#
#	by wangdd 2016/07/13
#
#该脚本主要用于Python2.6版本到2.7版本的自动升级,脚本中涉及到的软件版本可能会有变动根据实际情况修改即可

version_info=`python -V 2>/tmp/python_v.log`
current_v=`cat /tmp/python_v.log | grep 'Python 2.6'`
soft_path="/usr/local/src/soft"
[[ ! -d "$soft_path" ]] && mkdir -p $soft_path &>/dev/null


function get_soft(){
	echo "Start Download python2.7.12 from www.python.org,Please waiting...."
	wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz --no-check-certificate -P $soft_path
	echo "Start Download setuptools from pypi.python.org/packages/2.7/s/setuptools "
	wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg  --no-check-certificate -P $soft_path
	echo "Start Download pip-1.5.5 from github.com/pypa/pip/archive "
	wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz -P $soft_path
}

function install_soft(){
	yum instal -q -y gcc c++ zlib* openssl openssl-devel >/dev/null 2>&1
	cd $soft_path
	tar zxvf Python-2.7.12.tgz &>/dev/null
	cd Python-2.7.12
	./configure
	make all
	make install
	make clean
	make distclean
	[[ $? -eq 0 ]] && echo "python-2.7 install success" || exit
	mv /usr/bin/python /usr/bin/python2.6.6
	ln -s /usr/local/bin/python2.7 /usr/bin/python
	sed -i 's,#!/usr/bin/python,#!/usr/bin/python2.6,p' /usr/bin/yum
	
	#-------------------------------------------
	cd $soft_path
	chmod +x setuptools-0.6c11-py2.7.egg
	sh setuptools-0.6c11-py2.7.egg
	
	#------------------------------------------

	cd $soft_path
	tar zxvf 1.5.5 &>/dev/null
	cd pip-1.5.5
	python setup.py install
	mv /usr/bin/pip /usr/bin/pip2.6.6
	ln -s /usr/local/bin/pip /usr/bin/pip 
	
	[[ $? -eq 0 ]] && echo "pip-1.5 install success" || exit
	
}

if [ ! -z "$current_v" ];then
	get_soft
	install_soft
else
	echo "Current python version is : "`cat /tmp/python_v.log`
fi
