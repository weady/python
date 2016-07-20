from django.conf.urls import patterns,include,url
from auto_operation.views import *

urlpatterns = patterns('auto_operation.views',
	url(r'^$','login'),
	url(r'^index/$','index'),
	url(r'^command/$','command'),
	url(r'^file/$','trans_file'),
	url(r'^crontab/$','crontab'),
	url(r'domain/$','domain'),
	url(r'ilogslave/$','ilogslave'),
	url(r'servicedistribute/$','servicedistribute'),
)