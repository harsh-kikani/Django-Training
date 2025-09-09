from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.

def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('The PIN code must be exactly 6 digits.')

STATE_CHOICE = (
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('mp', 'mp'),
    ('gujarat', 'gujarat'),
    ('delhi', 'delhi'),
    
)

#--------------------create your models here--------------------------------------

class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=1)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(
        validators=[validate_pin_length],
        help_text='Enter 6-digit pin code')
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    mobile = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$')],
        help_text= "Enter a 10-digit mobile number"    
    )
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True,)
    my_file = models.ImageField(upload_to='doc', blank=True,)
    
    