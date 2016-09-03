#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import paramiko
import sys
import re
import time


class SshAuth:
    passinfo1 = 'yes/no'
    passinfo2 = 'password: '


    def __init__(self, source_host, dest_host, password, user='root', port=22):
        self.source_host = source_host
        self.dest_host = dest_host
        self.password = password
        self.user = user
        self.port = port

    def connect_source(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.source_host, username=self.user, port=self.port, password=self.password)

    def test_connet(self):
        channel = self.ssh.invoke_shell()
        channel.settimeout(4)

        buff = ''
        resp = ''
        channel.send('ssh '+self.user+'@'+self.dest_host+'\n')
        while not buff.endswith(self.passinfo2):
            try:
                resp = channel.recv(9999)
            except Exception, e:
                print 'Error info:%s connection time.' % (str(e))
                channel.close()
            buff += resp
            if not buff.find(self.passinfo1) == -1:
                channel.send('yes\n')
                buff = ''
            elif buff.endswith('# ') and re.findall('Connection timed out', buff):
                channel.close()
                print 'It can not connecting to: {}'.format(self.dest_host)
                break
            elif buff.endswith('# '):
                channel.close()
                break

        if buff.endswith(self.passinfo2):
            channel.close()
            return self.dest_host




    def build_ssh_auth(self, dest_host=None):
        if not dest_host:
            return None
        channel = self.ssh.invoke_shell()
        channel.settimeout(5)
        buff = ''
        tmp = ''

        channel.send('/bin/ls -l /root/.ssh/id_rsa /root/.ssh/id_rsa.pub\n')
        time.sleep(0.5)
        tmp = channel.recv(9999)
        if not re.findall('-r', tmp):
            channel.send('/usr/bin/ssh-keygen -P "" -t rsa -f "/root/.ssh/id_rsa"\n')
        else:
            channel.send('/usr/bin/ssh-copy-id ' + self.user + '@' + dest_host + '\n')
            tmp = channel.recv(9999)
            while not tmp.endswith(self.passinfo2):
                tmp += channel.recv(9999)
                if tmp.endswith(self.passinfo2):
                    channel.send(self.password + '\n')
                    time.sleep(0.5)
                    break
            channel.close()
            return None


        while not re.findall('\+-----------------\+', buff):
            try:
                resp = channel.recv(9999)
            except Exception,e:
                print 'Error info:%s connection time.' % (str(e))
                channel.close()
                self.ssh.connect()
                sys.exit()
            buff += resp
            if re.findall('\+-----------------\+', buff):
                channel.send('/usr/bin/ssh-copy-id '+self.user+'@'+dest_host+'\n')
                tmp = channel.recv(9999)
                while not tmp.endswith(self.passinfo2):
                    tmp += channel.recv(9999)
                    if tmp.endswith(self.passinfo2):
                        channel.send(self.password+'\n')
                        time.sleep(0.5)
                        break
                break
        channel.close()

    def ssh_close(self):
        self.ssh.close()


if __name__ == '__main__':
    source_host = '192.168.xxx'
    dest_host_list = ['xxxx','xxxx','xxxx']
    password = 'xxxxx'
    for dest_host in dest_host_list:
        sshauth = SshAuth(source_host, dest_host, password)
        sshauth.connect_source()
        tmp_dest_host = sshauth.test_connet()
        sshauth.build_ssh_auth(dest_host=tmp_dest_host)
        sshauth.ssh_close()

