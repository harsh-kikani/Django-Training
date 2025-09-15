"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from book.views import book, allbook, author, member, all_members, edit_book, delete_book, borrow, return_book, overdue, dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard,),
    path('book/', book, name='book'),
    path('book/all/', allbook, name='book'),
    path('author/', author, name='author'),
    path('member/', member, name='member'),
    path('member/all/',all_members),
    path('book/<int:id>/edit/', edit_book, name='edit_book'),
    path('book/<int:id>/delete/', delete_book, name='delete_book'),
    path('borrow/', borrow,),
    path('return/', return_book,),
    path('report/overdue/',overdue),
]
