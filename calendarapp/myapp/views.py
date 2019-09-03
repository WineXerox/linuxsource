from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

def index(req):
    return HttpResponse('สวัสดี')

def what(req):
    return HttpResponse('555')

def dosomething(req):
    return HttpResponse('I do nothing')

def myapp2(req):
  return render(req, 'myapp/myapp.html')




# Create your views here.
