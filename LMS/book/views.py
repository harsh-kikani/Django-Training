from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from book.forms import BookForm, AuthorForm, MemberForm, BorrowForm, ReturnForm
from book.models import Book, Member
from django.utils import timezone
from datetime import timedelta

# Create your views here.



def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'book/book.html', {'form':form})

def allbook(request):
    books = Book.objects.all()
    return render(request, "book/allBook.html", {"books": books})



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

def all_members(request):
    all_members = Member.objects.all()
    context = {
        'members': all_members,
    }
    return render(request, "book/allmember.html", context=context)



def edit_book(request, id):
    book = get_object_or_404(BookForm, id=id)
    author_name = None
    
    if request.method == "POST":
        title = request.POST.get("title")
        author_name = request.POST.get("author")
        category_name = request.POST.get("category")

        book.title = title
        book.category = category_name
        book.Is_available = request.POST.get("is_available") == "on"

        try:
            book.author = AuthorForm.objects.get(name=author_name)
        except AuthorForm.DoesNotExist:
            return render(request, 'book/editBook.html', {
                'text': 'Author not found'
            })

        book.save()

    return render(request, 'book/editBook.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(BookForm, id=id)
    if request.method == "POST":
        book.delete()
    return render(request, "book/deletebook.html", {"book": book})



def borrow(request):
    if request.method == 'POST':
        form =  BorrowForm(request.POST)
        if form.is_valid(): 
            book_name = form.cleaned_data["book_name"]
            member_name = form.cleaned_data["member_name"]
            issue_date = form.cleaned_data["issue_date"]
            due_date = issue_date + timedelta(days=15)
            
            try:
                book = Book.objects.get(title=book_name)
            except Book.DoesNotExist:
                return render(request, 'book/borrow.html', {
                    'form': form,
                    'msg': 'Book does not exist.'
                })

            try:
                member = Member.objects.get(name=member_name)
            except Member.DoesNotExist:
                return render(request, 'book/borrow.html', {
                    'form': form,
                    'msg': 'Member is not registred.'
                })

            if not book.Is_available:
                return render(request, 'book/borrow.html', {
                    'form': form,
                    'msg': 'Book is not available.'
                })

            if member.borrowed_books.count() >= 5:
                return render(request, 'book/borrow.html', {
                    'form': form,
                    'msg': 'Member has reached the borrow limit.'
                })

            book.issue_date = issue_date
            book.due_date = due_date
            book.member = member
            book.Is_available = False
            book.save()

            member.borrowed_books += 1
            member.save()
            return redirect('borrow')
    else:
        form = BorrowForm()
    return render(request, 'book/borrow.html', {'form':form})



def return_book(request):
    if request.method == "POST":
        form = ReturnForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]
            member_name = form.cleaned_data["member_name"]
            return_date = form.cleaned_data["return_date"] 
            try:
                book = BookForm.objects.get(title=book_name)
            except BookForm.DoesNotExist:
                return render(request, 'book/borrow.html', {
                    'form': form,
                    'msg': 'Book does not from our store.'
                })
            try:
                member = MemberForm.objects.get(name=member_name)
            except MemberForm.DoesNotExist:
                return render(request, 'book/borrowForm.html', {
                    'form': form,
                    'msg': 'Member is not registed.'
                })
            book.Is_available = True
            member.borrowed_books -= 1  
            book.return_date = return_date
           
            FINE_PER_DAY = 15 
            due_date = book.due_date 

            if return_date > due_date:
                late_days = (return_date - due_date).days
                fine = late_days * FINE_PER_DAY
                msg = f"Book returned late by {late_days} days. Fine: ₹{fine}"
                book.save()
                member.save()
                return render(request, "book/returnbook.html", {'form': form,'text': msg} )
            else:
                msg = "Book returned on time."
                book.save()
                member.save()
                return render(request, "book/returnbook.html", {'form': form, 'text':msg})
        
    else:
        form = ReturnForm()
    
    return render(request, "book/returnbook.html", {'form': form})


def overdue(request):
    overdue_books = Book.objects.filter(due_date__lt=timezone.now(), Is_available=False)
    context = {
        'overdue_books': overdue_books,
    }
    return render(request , "book/overdue.html", context=context)


def dashboard(request):
    all_books = Book.objects.all()  
    all_members = Member.objects.all()
    borrowed_books = Book.objects.filter(Is_available=False)
    overdue_books = Book.objects.filter(due_date__lt=timezone.now(), Is_available=False)


    context = {
        'books': all_books,
        'members': all_members,
        'borrowed_books': borrowed_books,
        'overdue_books': overdue_books,
    }
    return render(request, "book/dashboard.html", context=context)
