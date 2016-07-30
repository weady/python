from django.conf.urls import patterns,include,url
from auto_operation.views import *

urlpatterns = patterns('auto_operation.views',
	url(r'^$','login'),
	url(r'^index/$','index'),
	url(r'^hostcontral/$','hostcontral'),
	url(r'^record/$','recordmanage'),
	url(r'^dbmanage/$','dbmanage'),
	url(r'domain/$','domain'),
	url(r'servicedistribute/$','servicedistribute'),
	url(r'hostbaseinfo/$','hostbaseinfo'),
	url(r'configure/$','configure'),
)