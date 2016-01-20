from django.conf.urls import patterns,include,url

urlpatterns = [
	url(r'^$','monitor.views.first_page'),
	url(r'^table/','monitor.views.table'),
]
