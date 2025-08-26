from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home page')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1>Hello python<h1/>')

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_java(request):
    lang = '<h1>Hello java</h1>'
    return HttpResponse(lang)