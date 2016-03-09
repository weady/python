from django.conf.urls import patterns,include,url
from monitor.views import *

urlpatterns = patterns('monitor.views',
	url(r'^$','login'),
	url(r'^index/$','index'),
	url(r'^logout/$','logout'),
)
