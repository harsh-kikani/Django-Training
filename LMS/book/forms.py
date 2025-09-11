from django import forms
from book.models import Book, Author, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'category', 'author',]
        
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'join_date',]
        
class BorrowForm(forms.ModelForm):
    pass