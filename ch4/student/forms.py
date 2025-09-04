from django import forms
from django.core.validators import MinLengthValidator


# class Registration(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     city = forms.CharField()

class Registration(forms.Form):
    Name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    
    
#--------------Field Type example---------------
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),]

INTERESTS_CHOICES = [
    ('tech', 'Technology'),
    ('art', 'Art'),
    ('sports', 'Sports'),]

    
class DemoForm(forms.Form):
    # Basic fields
    name = forms.CharField()
    email = forms.EmailField()
    pin_code = forms.IntegerField()
    
    #Additional Field Types
    age = forms.FloatField()
    date_of_birth = forms.DateField()
    appointment_time = forms.TimeField()
    appointment_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms = forms.NullBooleanField()
    
    # Choice Fields
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    
    interests = forms.MultipleChoiceField(choices=INTERESTS_CHOICES)
    
    #File and url fields
    profile_image = forms.ImageField()
    resume = forms.FileField()
    website = forms.URLField()
    
    #other specialized fields
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    password = forms.CharField(widget=forms.PasswordInput())
    slug = forms.SlugField()
    ip_address = forms.GenericIPAddressField()
    rating = forms.DecimalField()
    
    
    
# class DemoForm(forms.Form):
#     name = forms.CharField(
#         label="Full Name",
#         max_length=100,
#         label_suffix=":",
#         initial="Enter your full name",
#         help_text="Enter your legal name here",
#         validators=[MinLengthValidator(3)]
#     )
    

    
    
    