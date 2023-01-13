from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,blank=False, primary_key=True,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)