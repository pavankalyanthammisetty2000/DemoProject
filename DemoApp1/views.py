from django.shortcuts import render;
from django.http import HttpResponse

#Create your views here...
def f1(request):
	return HttpResponse("<h1>Hello from DemoApp1 f1()</h1><hr />");
def f2(request):
	return HttpResponse("<h1>Hello from DemoApp1 f2()</h1><hr />");

def f111(request):
	return HttpResponse("<h1>Hello from DemoApp1 f111()</h1><hr />");


def f222(request):
	return HttpResponse("<h1>Hello from DemoApp1 f222()</h1><hr />");
