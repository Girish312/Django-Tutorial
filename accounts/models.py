from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser): #it's not a normal class, it's inheriting properties from AbstractUser class.
    pass

""" CustomUser inherits from AbstractUser, which already includes all standard authentication fields:
    - username
    - password
    - email
    - first_name
    - last_name
    - is_staff
    - is_active
    - date_joined
    So Django's built-in LoginView uses username and password from AbstractUser for authentication. 
    No extra fields needed unless you want to customize (e.g., use email instead of username)."""