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
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    join_date = models.DateField(default=date.today)
    borrowed_book = models.IntegerField(default=True)
    
    def __str__(self):
        return self.id

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Is_available = models.BooleanField(default=True)
    issue_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self):
        return self.id
    

# class BorrowRecord(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     issue_date = models.DateField()
#     due_date = models.DateField()
#     return_date = models.DateField()
#     fine = models.IntegerField()
    
#     def __str__(self):
#         return self.member