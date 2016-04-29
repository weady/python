#coding=utf-8
#ansible playbook笔记
#playbook格式,nginx.yml 文件内容
#********************************************************************
---
- hosts: webservers #定义操作的对象
  vars:	#为webservers组内的主机定义变量
  	worker_processes:4
  	num_cpus:4
  	max_open_file: 65506
  	root: /data
  remote_user:root	#指定远程操作的用户
  tasks:	#定义任务
  - name: ensure nginx is at the latest version
  	yum:pkg=nginx state=latest	#使用了yum 模块
  - name: write the nginx config file
  	template: src=/tmp/nginx2.conf dest=/etc/nginx/nginx.conf #利用template模块对本地配置模板进行渲染，并同步到目标主机
  	notify:	#定义handlers触发的动作名称
  	- restart nginx
  - name: ensure nginx is running
  	service: name=nginx state=started
  handlers:	#收到触发时执行一次命令
  	- name: restart nginx
  	  service: name=nginx state=restarted
#********************************************************************
#/tmp/nginx2.conf 配置文件模板内容,模板中可以应用playbook定义的变量
user nginx;
worker_processes {{ worker_processes}};
{% if num_cpus ==2 %}
worker_cpu_affinity 01 10;
{% elif num_cpus ==4 %}
worker_cpu_affinity 1000 0100 0010 0001;
{% elif num_cpus >=8 %}
worker_cpu_affinity 00000001 00000010 00000100 00001000 00010000 00100000 01000000 10000000;
{% else %}
worker_cpu_affinity 1000 0100 0010 0001;
{% endif %}
worker_rlimit_nofile {{ max_open_files }}
#********************************************************************
#playbook的执行
ansible-playbook test.yml -f 10 	//	启用10个并发进程数执行playbook
参数:
-u test //指定远程执行的用户
--syntax-check //检测playbook语法
--setp	//逐步执行
--list-hosts playbooks	//匹配到的主机列表
#********************************************************************
当多个playbook涉及复用的任务列表时，可以将复用的内容剥离出来，写到独立的文件中最后在需要使用的地方include
tasks:
	- include: wordpress.yml user=test01
	- include: wordpress.yml user=test02
tasks:
	- { include: wordpress.yml,user: test, ssh_keys:['keys/one.txt','keys/two.txt'] }
#********************************************************************
角色:
角色是ansible定制好的一种标准规范，以不同级别目录层次及文件对角色、变量、任务、处理程序等进行拆分
例子如下:
site.yml
webservers.yml
roles/
	common/
		files/
		templates/
		tasks/
		handlers/
		vars/
		meta
	webservers/
		files/
		templates/
		tasks/
		handlers/
		vars/
		meta/

在playbook中引用
site.yml
---
- hosts: webservers
  roles:
  	- common
  	- webservers

roles/x/tasks/main.yml	//其中列出的任务将被添加到执行队列
roles/x/handlers/main.yml 	//列出的处理程序将被添加到执行队列
roles/x/var/main.yml 	//列出的变量将被添加到执行队列

playbook 目录结构: 变量定义目录group_vars 主机组定义文件hosts 全局配置文件site.yml 角色功能目录

/home/test/ansible/playbook/nginx

nginx/hosts文件定义主机组，可以通过ansible-playbook -i hosts 调用
nginx/gourp_vars	//定义主机组变量
		all
		webservers
nginx/site.yml //主配置文件
---
- name: xxxx
  hosts: all
  roles:
  	- common
- name: xxxx
  hosts:webservers
  roles:
  	- web
#角色common定义
nginx/roles/
		common
			handlers
				main.yml 文件定义执行的命令
			tasks
				main.yml 文件定义任务列表，及利用ansible 各个模块执行相应的操作
			templates
				test.conf 定义模板文件
			vars
				main.yml 定义这个角色中模板所需要的变量，优先级大于全局的group_vars定义的变量
		web 角色的目录结构和common的类似
运行角色
cd /home/test/ansible/playbook/nginx
ansible-playbook -i hosts site.yml -f 10

#变量的定义
变量名的命名规则由字母、数字和下划线组合，必须以字母开头
jinja2过滤器
jinja2 是python 的一个广泛应用的模板引擎
使用格式:{{ 变量名|过滤方法 }}
{{ path | basename }}	//过滤出文件名
本地facts，通过-m setup 获取的关于主机的信息
{{ ansible_local.preferences.general.open_files }}	//类似这样的引用
#注册变量
变量的另一个用途是将一个命令的运行结果保存到变量中，供后面的playbook使用
eg：
- hosts:webservers
  tasks:
  	- shell:/usr/bin/foo
  	register:foo_result
  	ignore_errors:True

    - shell:/usr/bin/bar
      when: foo_result.rc ==5	#/usr/bin/foo的命令执行后的rc==5才会执行/usr/bin/bar

条件语句
when:result|success 表示当变量result执行结果为成功状态时，执行相应的命令
循环:
- name: add users
  user: name={{ item }} state=present groups=wheel
  with_items: #with_times会自动循环执行user:xxxx 命令，循环的次数时下面的变量个数
  		- testuser1
  		- testuser2

  with_items:
  	- {name:'test1',groups:'group1'} #可以是字典
  with_flattened:	#如果是列表就用with_flattened
  	- ['test1','test2']	

总结:
	一个典型的playbook的目录结构为:
	playbook_name	#playbook的目录，一般位于/etc/ansible/目录下
    ├── group_vars	#定义变量的目录，可以对不同roles定义不同的变量文件
    ├── hosts #定义主机的信息
    ├── roles	#定义不同类型的角色，进行不同的配置
    │   ├── db	#db角色
    │   │   ├── files
    │   │   │   └── epel.repo	#要复制的yum 仓库文件
    │   │   ├── handlers	#执行程序目录
    │   │   │   └── main.yml
    │   │   ├── tasks
    │   │   │   └── main.yml
    │   │   └── templates	#模板的存放目录，
    │   │       └── my.cnf.j2 #模板文件，可以使用if...endif for endfor 以及引用变量等
    │   └── web #web角色
    │       ├── handlers
    │       ├── tasks
    │       └── templates
    └── site.yml	#该playbook的入口文件


