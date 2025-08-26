from django.contrib import admin
from django.urls import path
from app1.views import learn_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('py/', learn_django),
    path('dj/', learn_django, {'status': 'ok'}),
]