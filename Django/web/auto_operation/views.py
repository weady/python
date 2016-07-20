#coding=utf-8
#
#	by wangdd 2016/03/09
#

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import subprocess
import re
from auto_operation.bin import base
import platform
#验证用户是否登录的装饰器

def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return view(request, *args, **kwargs)
    return new_view

#注册
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username=username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('index.html')

#登录
def login(request):
    error = False
    if request.method == 'POST':     #我们使用POST的方法来获取从HTML传递过来的表单内容
        username = request.POST['username']           #获取账号和密码
        password = request.POST['password']
        #获取的表单数据与数据库进行比较
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                #比较成功，跳转到index
                response = HttpResponseRedirect('index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username)
                return response
        else:
            #比较失败，还在login
            error = True

    return render_to_response('login.html',{'error': error})


#退出
def logout(request):
    response = HttpResponseRedirect('/monitor')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#@requires_login
def index(request):
	return render_to_response('index.html')
#执行主机目录，通过/etc/hosts获取到主机列表
def command(request):
    hostname=base.get_host_lists()
    local_name=platform.node()
    if request.method == "POST":
        data=request.POST['cmd']
        host=request.POST['host_name']
        if re.search(r'(rm)',data,re.I):
            result="这是个危险命令" 
            return HttpResponse(result)
        elif data == "" or host == "":
            result = "请选择主机或输入命令"
            return HttpResponse(result)
        else:
            if host == local_name:
                disk = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
                return HttpResponse(disk.stdout.readlines())
            else:

                return HttpResponse(host)
    return render_to_response('exec_cmd.html',{'names':hostname})

#文件的上传和下载
def trans_file(request):
    return render_to_response('transfile.html')
#计划任务
def crontab(request):
    return render_to_response('crontab.html')
#域名管理
def domain(request):
    domain_lists=base.get_domain_info()
    return render_to_response('domain.html',{'domain_info':domain_lists})
#ilogslave
def ilogslave(request):
    return render_to_response('ilogslave.html')
#云平台的服务分布
def servicedistribute(request):
    servicedistribute_lists = base.get_service_distribute()
    return render_to_response('service_distribution.html',{'service_info':servicedistribute_lists})