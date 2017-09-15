#coding=utf-8

#	by wangdd 2016/03/17

#pexpect 模块实现自动化交互
#spawn 类
#expect方法的两个成员before after;before 成员保存了最近匹配成功之前的内容,after成员保存了最近匹配成功之后的内容
#run 函数
#pxssh 类是pexpect的派生类，针对在ssh会话操作上做一层封装
#pxssh 常用的3个方法:login() 建立ssh连接   logout() 断开连接 prompt()	等待系统提示符,用于等待命令执行结果

import sys
import pexpect
def auto_ssh():
	proc = pexpect.spawn('/usr/bin/ssh wangdong@192.168.1.200')
	fout = file('mylog.txt','w')
	proc.logfile = fout
	#proc.logfile = sys.stdout

	proc.expect("password:")
	proc.sendline("wangdong")
	proc.expect('$')
	proc.sendline('ls /home')
	proc.expect('$')

def auto_ftp():
	proc = pexpect.spawn('ftp ftp.xxx.cn')
	proc.expect('(?i)name .*:')	#(?i) 表示后面的字符串正则匹配忽略大小写
	proc.sendline('用户名')
	proc.expect('(?i)password')
	proc.sendline('密码')	#ftp密码
	proc.expect('ftp>')
	proc.sendline('bin')
	proc.expect('ftp>')
	proc.sendline('cd soft')
	proc.expect('ftp>')
	proc.sendline('get my.cnf')	#下载响应的文件
	proc.expect('ftp>')
	sys.stdout.write(proc.before)
	print 'Escape character is "^]".\n'
	sys.stdout.write(proc.after)
	sys.stdout.flush()
	proc.interact()
	proc.sendline('bye')
	proc.close()

#实现远程主机上的文件打包，传输到本地
def auto_tar_file():
	ip = ""
	user = ""
	password = ""
	target_file = "/usr/local/www"

	proc = pexpect.spawn('ssh',[user+'@'+ip])
	fout = file('log.txt','w')
	pexpect.logfile = fout

	try:
		proc.expect('(?i)password')
		proc.sendline(password)
		proc.expect('#')
		proc.sendline('tar -czf /usr/local/src/www.tar.gz'+target_file)

		proc.expect('#')
		print proc.before
		proc.sendline('exit')
		fout.close()
	except EOF:
		print 'expect EOF'
	except TIMEOUT:
		print 'expect TIMEOUT'

	proc = pexpect.spawn('/usr/bin/scp',[user+'@'+ip+':/usr/local/src/www.tar.gz','/home'])
	fout = file('log.txt','w')
	proc.logfile = fout

	try:
		proc.expect('(?i)password')
		proc.sendline(password)
		proc.expect(pexpect.EOF)	#匹配缓存区EOF，保证文件复制正常完成
	except EOF:
		print 'expect EOF'
	except TIMEOUT:
		print 'expect TIMEOUT'



import pexpect
import getpass, os

#user: ssh 主机的用户名
#host：ssh 主机的域名
#password：ssh 主机的密码
#command：即将在远端 ssh 主机上运行的命令

def ssh_command (user, host, password, command):

    ssh_newkey = 'Are you sure you want to continue connecting'
    # 为 ssh 命令生成一个 spawn 类的子程序对象.
    child = pexpect.spawn('ssh -l %s %s %s'%(user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    # 如果登录超时，打印出错信息，并退出.
    if i == 0: # Timeout
        print 'ERROR!'
        print 'SSH could not login. Here is what SSH said:'
        print child.before, child.after
        return None
    # 如果 ssh 没有 public key，接受它.
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        child.expect ('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
                print 'ERROR!'
                print 'SSH could not login. Here is what SSH said:'
                print child.before, child.after
                return None
    # 输入密码.
    child.sendline(password)
    return child
def main ():
    # 获得用户指定 ssh 主机域名.
    host = raw_input('Hostname: ')
    # 获得用户指定 ssh 主机用户名.
    user = raw_input('User: ')
    # 获得用户指定 ssh 主机密码.
    password = getpass.getpass()
    # 获得用户指定 ssh 主机上即将运行的命令.
    command = raw_input('Enter the command: ')
    child = ssh_command (user, host, password, command)
    # 匹配 pexpect.EOF
    child.expect(pexpect.EOF)
    # 输出命令结果.
    print child.before

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)