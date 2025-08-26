from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myapp2(request):
    return HttpResponse('My app 2 page')


def myapp2_me(request):
    return HttpResponse('My app 2 Me page')