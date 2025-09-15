from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    
    def __str__(self):
        return self.name 
    
    
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    join_date = models.DateField(default=date.today)
    borrowed_book = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Is_available = models.BooleanField(default=True)
    
    # member = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrowed_books')

    issue_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    

