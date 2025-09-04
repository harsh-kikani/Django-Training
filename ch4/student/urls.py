from django.urls import path
from student.views import registration, login, demo_form, reg_success

urlpatterns = [
    path('register/', registration, name ='registration'),
    path('login/', login, name ='login'),
    path('demo-form/', demo_form, name='demo_form'),
    path('success/', reg_success, name ='reg_success'),
    
]
