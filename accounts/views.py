from django.shortcuts import render, redirect # importing the render and redirect functions from django.shortcuts module. render is used to render HTML templates with context data, and redirect is used to redirect the user to a different URL.
from .forms import CustomUserCreationForm # importing the CustomUserCreationForm from the current app's forms.py file.
# Create your views here.

def signup(request): # defining a view function named signup that takes an HTTP request as an argument.
    if request.method == 'POST': # checking if the request method is POST, which indicates that the form has been submitted.
        form = CustomUserCreationForm(request.POST) # creating an instance of CustomUserCreationForm with the submitted data.
        if form.is_valid(): # checking if the form data is valid according to the form's validation rules.
            form.save() # saving the new user to the database if the form is valid.
            return redirect('login') # redirecting the user to the login page after successful registration.
    else: # if the request method is not POST (i.e., it's a GET request), it means the user is accessing the signup page for the first time.
        form = CustomUserCreationForm() # creating an empty instance of CustomUserCreationForm to display in the template.

    data = {'form': form} # creating a context dictionary to pass the form instance to the template.
    return render(request, 'accounts/login.html', data) # rendering the signup.html template and passing the form instance to it for display.