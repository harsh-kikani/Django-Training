from django.shortcuts import render
from student.forms import Registration, TeacherRegistration, Login, DemoForm
from django.http import HttpResponseRedirect
from student.models import Profile
# Create your views here.



# def registration(request):
#     if request.method == 'POST':
#         form = Registration(request.POST)
        
#         if form.is_valid():
#             nm = form.cleaned_data['name']
#             em = form.cleaned_data['email']
#             pw = form.cleaned_data['password']
#             cpw = form.cleaned_data['confirm_password']
#             print('name:', nm)
#             print('Email:', em)
#             print('Password:', pw)
#             print('Confirm_Password:', cpw)
           
#             # Save Data into Database
#             user = Profile(name=nm, email=em, password=pw)
#             user.save()
            
#             #Update Data into Database
#             # user = Profile(id=1, name=nm, email=em, password=pw)
#             # user.save()
            
#             # Delete Data into Database
#             # user = Profile(id=1)
#             # user.delete()
            
#             return HttpResponseRedirect('/student/register/')
#             # return HttpResponseRedirect('/student/success/')
            
#     else:    
#         form = Registration()
#     # fm = Registration(field_order=['email', 'city'])
#     return render(request, 'student/registration.html', {'form': form})




# def Teacher_registration(request):
#     if request.method == 'POST':
#         form = TeacherRegistration(request.POST)
#         if form.is_valid():
#             nm = form.cleaned_data['name']
#             em = form.cleaned_data['email']
#             pw = form.cleaned_data['password']
#             cpw = form.cleaned_data['confirm_password']
#             print('name:', nm)
#             print('Email:', em)
#             print('Password:', pw)
#             print('Confirm_Password:', cpw)
            
#             # Save Data into Database
#             user = Profile(name=nm, email=em, password=pw)
#             user.save()
            
#             return HttpResponseRedirect('/student/register/')
#     else:    
#         form = TeacherRegistration()
#     # fm = Registration(field_order=['email', 'city'])
#     return render(request, 'student/teacher_reg.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Registration()
    return render(request, 'student/registration.html', {'form': form})

def Teacher_registration(request):
    if request.method == 'POST':
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherRegistration()
    return render(request, 'student/teacher_reg.html', {'form': form})
    
#-----------------save data second method-------------------------------------

# def registration(request):
#     if request.method == 'POST':
#         obj = Profile.object.get(pk=2)
#         form = Registration(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
        
        
    #         return HttpResponseRedirect('/student/register/')
    #         # return HttpResponseRedirect('/student/success/')
            
    # else:    
    #     form = Registration()
    # # fm = Registration(field_order=['email', 'city'])
    # return render(request, 'student/registration.html', {'form': form})



def reg_success(request):
    return render(request, 'student/success.html')




def login(req):
    fm = Login()
    
    # fm = Login(auto_id='rohan_%s')
    # fm = Login(auto_id=True)
    # fm = Login(auto_id=False)    
    # fm = Login(auto_id='mehul')
    
    # fm = Login(label_suffix='A') 
    # fm = Login(label_suffix=' ') 
    
    # fm = Login(initial={'email': 'mehul@example.com',
    #                     'password': '1234'})
    
    # fm = Login(auto_id='mehul_%s', label_suffix='A', initial={
    #     'email': 'mehul@example.com','password': '1234'})
    
    return render(req, 'student/login.html', {'form': fm})



#------------------DEMOFORM--------------------

def demo_form(request):
    form = DemoForm()
    return render(request, 'student/demoform.html', {'form': form})

