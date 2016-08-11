#coding=utf-8
#
#	by wangdd 2016/03/09
#

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,InvalidPage,EmptyPage #分页
import json
from django.http import JsonResponse
import subprocess
import re
from auto_operation.bin import baseclass #自定义的类
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
#--------------------------云平台管理模块-----------------------------------
#主机管理子模块
#1.执行命令
def hostcontral(request):
    hostlist = []   #存储执行命令的主机
    key_list = ['f_hostname']
    database_sql = baseclass.db_sql()
    hostnames_sql = database_sql.get_s_sql('t_host_info',key_list)
    srvgroup_sql = "select f_servername from t_service_distribution group by f_servername having f_servername not like 'mysql'"
    hostnames = database_sql.db_connect('root','123456','192.168.36.108','auto_operation',hostnames_sql)
    grouplists = database_sql.db_connect('root','123456','192.168.36.108','auto_operation',srvgroup_sql)

    if request.method == "POST":
        data=request.POST['cmd']
        host=request.POST['hostname']
        group = request.POST['groupname']
        if re.search(r'rm|reboot|shutdown|init 0|init 6',data,re.I):
            result="这是个危险命令" 
            return HttpResponse(result)
        elif data == "":
            result = "请输入命令"
            return HttpResponse(result)
        else:
            if host and data:
                hostlist.append(host)
                #实例化SSH连接
                SSHConection = baseclass.sshconn(hostlist,'root',data)
                result = SSHConection.sshentrance()
                return HttpResponse(result)
            if group and data:
                sql = "select distinct f_hostname from t_service_distribution where f_servername = '%s'" % group
                host = database_sql.db_connect('root','123456','192.168.36.108','auto_operation',sql)
                for h in host:
                    hostlist.append(h[0])                 
                SSHConection = baseclass.sshconn(hostlist,'root',data)
                result = SSHConection.sshentrance()
                # for item in result:
                return HttpResponse(result)
    return render_to_response('execcmd.html',{'names':hostnames,'groups':grouplists})
#2.文件同步

#3.定时任务
def crontab(request):
    return render_to_response('crontab.html')
#4.无密配置


#录流管理子模块
def recordmanage(request):
    return render_to_response('recordmanage.html')
#数据库管理子模块
def dbmanage(request):
    return render_to_response('dbmanage.html')
#域名管理子模块
def domain(request):
    select_dict = {}
    select_value = ""
    search = ""
    database_sql = baseclass.db_sql()
    key_list = ['domain_name','domain_info','domain_type','domain_modified_time']
    sql = database_sql.get_s_sql('dns_domain_info',key_list,selecttype='vague')

    if request.method == 'POST':
        select_value = request.POST['conditions']
        search = request.POST['searchname']
        if search and select_value:
            select_dict[select_value] = search
        if search != "" and select_value != "":
            sql = database_sql.get_s_sql('dns_domain_info',key_list,select_dict,selecttype='vague')
        else:
            sql = sql
    else:
        if request.GET.get('value') and request.GET.get('search'):
            select_value = request.GET.get('value')
            search = request.GET.get('search')
            select_dict[select_value] = search
            sql = database_sql.get_s_sql('dns_domain_info',key_list,select_dict,selecttype='vague')
        else:
            sql = sql
        

    domain_sql_result = database_sql.db_connect('root','xxx','192.168.xxx.xxx','database',sql)
    ONE_PAGE_OF_DATA = 20 
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    #判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = domain_sql_result[startPos:endPos]
    List=[]
    for i in range(1,len(posts)):
        for d in posts:
            a = list(d)
            a.insert(0,i)
        List.append(a)

    if curPage == 1 and allPage == 1: #标记1
        allPostCounts = len(domain_sql_result)
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1
    return render_to_response('domain.html',{'domain_info':List,'allPage':allPage, 'curPage':curPage,'selectvalue':select_value,'searchvalue':search})

#--------------------------云平台业务分布模块-----------------------------------
#云平台的服务分布
def servicedistribute(request):
    select_dict = {}
    select_value = ""
    search = ""
    #实例化数据库操作
    database_sql = baseclass.db_sql()
    key_list = ['f_clustername','f_hostname','f_servername','f_serverid','f_status','f_function','f_description']
    sql = database_sql.get_s_sql('t_service_distribution',key_list,select_dict,selecttype='vague')
    

    if request.method == 'POST':
        select_value = request.POST['conditions']
        search = request.POST['searchname']
        if search and select_value:
            select_dict[select_value] = search
        if search != "" and select_value != "":
            sql = database_sql.get_s_sql('t_service_distribution',key_list,select_dict,selecttype='vague')
        else:
            sql = sql
    else:
        if request.GET.get('value') and request.GET.get('search'):
            select_value = request.GET.get('value')
            search = request.GET.get('search')
            select_dict[select_value] = search
            sql = database_sql.get_s_sql('t_service_distribution',key_list,select_dict,selecttype='vague')
        else:
            sql = sql

    servicedistribute_lists = database_sql.db_connect('root','123456','192.168.36.108','auto_operation',sql)
    ONE_PAGE_OF_DATA = 20 
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    #判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = servicedistribute_lists[startPos:endPos]

    if curPage == 1 and allPage == 1: #标记1
        allPostCounts = len(servicedistribute_lists)
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render_to_response("servicedistribution.html",{'service_info':posts, 'allPage':allPage, 'curPage':curPage,'selectvalue':select_value,'searchvalue':search})

#云主机的基本信息
def hostbaseinfo(request):
    select_dict = {}
    select_value = ""
    search = ""
    #实例化数据库操作
    database_sql = baseclass.db_sql()
    key_list = ['f_clustername','f_hostname','f_liip','f_hiip','f_loip','f_hoip','f_description']
    sql = database_sql.get_s_sql('t_host_info',key_list,select_dict,selecttype='accurate')
    
    if request.method == 'POST':
        select_value = request.POST['conditions']
        search = request.POST['searchname']
        if search and select_value:
            select_dict[select_value] = search
        if search != "" and select_value != "":
            sql = database_sql.get_s_sql('t_host_info',key_list,select_dict,selecttype='accurate')
        else:
            sql = sql

    servicedistribute_lists = database_sql.db_connect('root','123456','192.168.36.108','auto_operation',sql)
    ONE_PAGE_OF_DATA = 20 
    try:
        curPage = int(request.GET.get('curPage', '1'))
        allPage = int(request.GET.get('allPage','1'))
        pageType = str(request.GET.get('pageType', ''))
    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    #判断点击了【下一页】还是【上一页】
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = servicedistribute_lists[startPos:endPos]

    if curPage == 1 and allPage == 1: #标记1
        allPostCounts = len(servicedistribute_lists)
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render_to_response("hostbaseinfo.html",{'hostbaseinfo':posts, 'allPage':allPage, 'curPage':curPage,'selectvalue':select_value,'searchvalue':search})

#--------------------------设置模块-----------------------------------
#excel数据导入到数据库
def configure(request):
    return render_to_response('configure.html')
