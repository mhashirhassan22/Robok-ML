from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    company = models.CharField(max_length=255)
    business_case = models.CharField(max_length=1000)

class ImageRequest(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="image_user")
    uploaded_image = models.ImageField(upload_to='media/')
    result = models.ImageField(upload_to='media/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    infer_time = models.IntegerField(default=0)