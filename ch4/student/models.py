# from django.db import models

# # Create your models here.


# class Profile(models.Model):
#     name = models.CharField(max_length=70)
#     roll = models.IntegerField()
#     email = models.EmailField(max_length=255)
#     city = models.CharField(max_length=70)
    
#     # def __str__(self):
#     #     return self.name
    
    
#     # def __str__(self):
#     #   return str(self.roll)
     
# class Result(models.Model):
#     stu_class = models.CharField(max_length=70)
#     marks = models.IntegerField()
    
#     # def __str__(self):
#     #     return str(self.stu_class)


from django.db import models

#Create your models here.

# class Profile(models.Model):
#     name = models.CharField(max_length=20, blank=True)
#     email = models.EmailField(max_length=255)
#     password = models.CharField(max_length=20)

class Profile(models.Model):
    student_name = models.CharField(max_length=100, blank=True, null=True)
    teacher_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    