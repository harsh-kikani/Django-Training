from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from book.forms import BookForm, AuthorForm, MemberForm, BorrowForm

# Create your views here.

def home(request):
    return HttpResponse("<h2>hello<h2>")

def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book/base.html', {'form':form})


def author(request):
    if request.method == 'POST':
        form =  AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = AuthorForm()
    return render(request, 'book/author.html', {'form':form})

def member(request):
    if request.method == 'POST':
        form =  MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = MemberForm()
    return render(request, 'book/member.html', {'form':form})


def borrow(request):
    if request.method == 'POST':
        form =  BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow')
    else:
        form = BorrowForm()
    return render(request, 'book/member.html', {'form':form})

