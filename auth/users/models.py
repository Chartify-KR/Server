from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    
    USERNAME_FIELD = 'email' #예제에서는 email로 로그인을 원함/ 장고는 username으로 로그인하는 편
    REQUIRED_FIELDS = []
# Create your models here.
