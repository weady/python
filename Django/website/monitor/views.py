from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from monitor.models import Hosts
#coding=utf-8
# Create your views here.

#def first_page(request):
#	host_list = Hosts.objects.all().values('host').order_by("name").exclude(host='Discovery')
#	return render_to_response('host.html',{'host_name':host_list})
def first_page(request):
	return render_to_response('index.html')
def table(request):
	host_list = Hosts.objects.all().values('host','hostid').order_by("name").exclude(host='Discovery')
	return render_to_response('table.html',{'host_name':host_list})
