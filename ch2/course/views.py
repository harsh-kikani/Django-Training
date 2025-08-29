from django.shortcuts import render


# Create your views here.

#def learn_django(req):
    
    #return render(req, template_name, context=dic_name,
    #content_type=MIME_TYPE, status=None, using=None)
    
 #   return render(req, 'course/django.html')

#def learn_fastapi(req):
#    return render(req, 'course/fastapi.html')

# Example 1.1 - Variable

#def learn_django(req):
#    return render(req, 'course/django.html', context={'name': 'Django'})


# Example 1.2 - Variable
#def learn_django(req):
#    return render(req, 'course/django.html', context={'name': 'Django'})


def learn_django(req):
    return render(req, 'course/django.html', {'nm': 'Django 5.x'})