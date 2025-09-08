from django.urls import path
from student.views import registration, Teacher_registration, login , demo_form, reg_success

urlpatterns = [
    path('register/', registration, name ='registration'),
    path('tea-register/', Teacher_registration, name="Teacher_registration"),
    path('login/', login, name ='login'),
    path('demo-form/', demo_form, name='demo_form'),
    path('success/', reg_success, name ='reg_success'),
    
]
