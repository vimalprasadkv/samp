from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    userType=models.CharField(max_length=30)
class Cu_user(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.CharField(max_length=10)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)