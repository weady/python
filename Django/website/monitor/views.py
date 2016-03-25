#coding=utf-8
#
#	by wangdd 2016/03/09
#

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
def hosts(request):
	return render_to_response('host_contral.html')
