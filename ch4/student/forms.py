from django import forms
from django.core import validators
from student.models import Profile




# class Registration(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     city = forms.CharField()

# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
    
# class Login(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField()
    
    
    
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
    
    
    
class DemoForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        max_length=100,
        label_suffix=":",
        initial="Enter your full name",
        help_text="Enter your legal name here",
        validators=[validators.MinLengthValidator(3)]
    )
    


#---------------------Login------------------------------------

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    
    
    
#-------------------Registration---------------------------------------
    
# class Registration(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)


    #--------Form Validation specific Field----------------
    
    
#     def clean_name(self):
#         # name_value = self.cleaned_data.get('name')
#         name_value = self.cleaned_data['name']
#         if len(name_value) < 4:
#             raise forms.ValidationError('Enter more than or equal 4 char')
#         return name_value
    
#     def clean_email(self):
#         email_value = self.cleaned_data['email']
#         if len(email_value) < 20:
#             raise forms.ValidationError('Enter more than or equal 20 char')
#         return email_value
    
    

#---------------Form Validate All at Once----------------

# class Registration(forms.Form):
#     Name = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
    
#     def clean(self):
#         cleaned_data = super().clean()
#         name_value = cleaned_data.get('Name')
#         email_value = cleaned_data.get('email')
        
#         if name_value and len(name_value) < 4:
#             self.add_error('Name', 'Enter more than or equal to 4 characters')
            
#         if email_value and len(email_value) < 20:
#             self.add_error('email', 'Enter more than or equal to 20 characters')

#         return cleaned_data
    
    
    
    
#-----------------Form Built-in Validator and Custom Validator--------------------------------------------

# def starts_with_s(value):
#     if value[0] != 's':
#         raise forms.ValidationError('Email should start with s')
    
# class Registration(forms.Form):
#     Name = forms.CharField(
#         validators=[
#             validators.MaxLengthValidator(10),
#             validators.MinLengthValidator(3)
#         ])
#     email = forms.EmailField(validators=[starts_with_s])
#     password = forms.CharField(widget=forms.PasswordInput)
    


# class Registration(forms.Form):
#     name = forms.CharField(error_messages={'required': 'Name is Required'})
#     email = forms.EmailField(
#         error_messages={'required': 'Email is Required'},
#         min_length=5, max_length=50)
#     password = forms.CharField(
#         error_messages={'required': 'Password is Required'},
#         widget=forms.PasswordInput, min_length=5, max_length=50)





class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    confirm_password = forms.CharField()
    class Meta:
        model = Profile
        #fields = ['name', 'email', 'password']
        fields = '__all__'
        
        labels = {
            'name': 'Enter Name', 
            'email': 'Enter Email'
        }
        error_messages = {
            'email': {'required': 'Email is required'}
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'pwdclass'}),
            'name': forms.TimeInput(attrs={'class':'myclass','placeholder': 'Enter your name'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'cpwclass'})
        }
        