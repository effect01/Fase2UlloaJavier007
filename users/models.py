from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    CODES_PHONE = (
        ('CHL +56',56),
        ('ARG +56',2),
        ('BRZ +56',3),
        ('USA',4),
        ('COL',5),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    code_number = models.CharField(   
            choices=CODES_PHONE,
            max_length=12,
            ) 
    phone_number = models.IntegerField()