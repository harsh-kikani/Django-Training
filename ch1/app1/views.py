from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def learn_django(req, **kwargs):
    status = kwargs.get('status','Not Allowed')
    return HttpResponse(f'<h1>Hello Django - app1<h1/>')



