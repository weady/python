#!/usr/bin/python
#
#
#
import smtplib
user = "wangdd"
password = "Wangdong123"
host = "smtp.iPanel.cn"
port = 25
sender = 'wangdd@iPanel.cn'
receivers = ['708964732@qq.com']
 
message = """From: From Person <wangdd@iPanel.cn>
To: To Person <708964732@qq.com>
Subject: SMTP e-mail test
 
This is a test e-mail message.
"""
def smp_mail(): 
    try:
       server = smtplib.SMTP() 
       server.connect(host,port)
       server.login(user,password)
       server.sendmail(sender, receivers, message)         
       server.quit()
       print "Successfully sent email"
    except Exception,e:
       print "Error: unable to send email"
if __name__ == '__main__':
    smp_mail()

