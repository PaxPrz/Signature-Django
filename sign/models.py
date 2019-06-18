from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Custom_user(AbstractUser):
    photo = models.ImageField(upload_to='user_photo')
    #cv = models.FileField(upload_to='user_cv')
    #phone_no = models.CharField(max_length=20)
    email = models.EmailField(unique=True)