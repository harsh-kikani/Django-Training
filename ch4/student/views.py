from django.shortcuts import render
from student.forms import Registration, Login, DemoForm
from django.http import HttpResponseRedirect

# Create your views here.



def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
            return HttpResponseRedirect('/student/success/')
            
    else:    
        form = Registration()
    # fm = Registration(field_order=['email', 'city'])
    return render(request, 'student/registration.html', {'form': form})

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

