from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_time(request):
    current_time = datetime.datetime.now()
    return render_to_response('time.html', locals())
