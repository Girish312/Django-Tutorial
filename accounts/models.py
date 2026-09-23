from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): #it's not a normal class, it's inheriting properties from AbstractUser class.
    pass