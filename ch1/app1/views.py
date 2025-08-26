from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def learn_django(req, **kwargs):
    status = kwargs.get('status','Not Allowed')
    return HttpResponse(f'<h1>Hello Django {status}<h1/>')

def learn_python(request):
    return HttpResponse('<h1>Hello python<h1/>')

