from django.shortcuts import render
from student.forms import ProfileForm
from student.models import Profile

# Create your views here.


# def home(request):
#     context = {'data': 'Hello I am django developer. I am also creating educational videos. I am not human.'}
#     return render(request, 'student/home.html', context)


def home(request):
    form = ProfileForm()
    return render(request, 'student/home.html', {'form':form})