from django import forms
from book.models import Book, Author, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'category', 'author',]
        
class edit_book(forms.Form):
    pass
        
        
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'join_date',]
        
class BorrowForm(forms.Form):
    book_name = forms.CharField()
    member_name = forms.CharField()
    issue_date = forms.DateField()
    
    
class ReturnForm(forms.Form):
    book_name = forms.CharField()
    member_name = forms.CharField()
    return_date = forms.DateField()