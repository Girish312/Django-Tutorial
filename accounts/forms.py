from django.contrib.auth.forms import UserCreationForm # built-in form that handles username and password validation, matching passwords, and secure password hashing.
from .models import CustomUser # importing the CustomUser model from the current app's models.py file.

class CustomUserCreationForm(UserCreationForm):
    class Meta: # Meta class is used to specify metadata for the form, such as the model it is associated with and the fields to include in the form.
        model = CustomUser # specifying that this form is associated with the CustomUser model.
        fields = ['username', 'email'] # defining the fields to be included in the form. In this case, only 'username' and 'email' are included.
