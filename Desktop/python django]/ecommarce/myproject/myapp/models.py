from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class customuser(AbstractUser):
    
    USER_TYPES=[
        ('Seller','Seller'),
        ('Customer','Customer'),
        ('Admin','Admin'),
    ]
    fullname=models.CharField(max_length=200,null=True)
    user_type=models.CharField(choices=USER_TYPES,max_length=200,null=True)
    
def __str__(self):
    return str(self.username)

    
    
    