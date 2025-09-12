from django.shortcuts import render
from django.contrib import messages
from .forms import StudentRegistration
# Create your views here.


def home(request):
    # messages.add_message(request, messages.SUCCESS,
    #                      'Your account has been created !!')
    # messages.add_message(request, messages.INFO,
    #                      'This is info !!')
    # messages.add_message(request, messages.WARNING,
    #                      'This is warning !!')
    # messages.add_message(request, messages.ERROR,
    #                      'This is error !!') 
    
    
    messages.success(request, 'This is Success !!!')
    messages.info(request, 'This is Info !!!')
    messages.warning(request, 'This is Warning !!!')
    messages.error(request, 'This is Error !!!')
    messages.debug(request, 'This is Debug !!!')
    print(messages.get_level(request))
    messages.set_level(request,messages.DEBUG)
    messages.debug(request, 'this is Debug after set !!!')
    
    return render(request,'student/home.html')

def registration(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Registration Success!!!')
    else:
        fm = StudentRegistration
    return render(request,'student/registration.html',
    {'form': fm})
