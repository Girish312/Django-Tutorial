"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # importing admin module from django.contrib package
from django.urls import path # importing path function from django.urls module
from invoices import views as invoices_views # importing views from invoices app and renaming it as invoices_views to avoid naming conflicts with the views module from the accounts app.
from django.contrib.auth import views as auth_views # importing views from django.contrib.auth package and renaming it as auth_views to avoid naming conflicts with the views module from the invoices app.
from accounts import views as accounts_views # importing views from accounts app and renaming it as accounts

# Tip: You can create a specific URL for each view function or class-based view in your Django application. This allows you to map different URLs to different views, enabling users to access various parts of your application through distinct URLs.
""" 
1) create a new file called urls.py in the invoices app directory.
2) In the urls.py file, import the necessary modules and define the URL patterns for the invoices app.
3) In the mysite/urls.py file, include the invoices app's URL patterns using the include() function. This allows you to organize your URLs and keep the main URL configuration clean and manageable.
Example:
from django.urls import include, path
urlpatterns = [
    path('', include('invoices.urls')),
    path('admin/', admin.site.urls),
] """

urlpatterns = [
    # path('address/', view_function, name= 'nickname')
    path('admin/', admin.site.urls), # This line maps the URL path 'admin/' to the Django admin site. When a user visits 'http://<your-domain>/admin/', they will be directed to the admin interface provided by Django.
    path('cus_name/', invoices_views.show_invoice, name='cus_name'),
    # Note: you don't have to use () after show_invoice because django will do it internally when the URL is accessed.
    path('', invoices_views.LandingPageView.as_view(), name='landing'),
    path('home/', invoices_views.HomePageView.as_view(), name='home'),
    path('base/', invoices_views.BasePageView.as_view(), name='base'),
    # Note: you have to use .as_view() after class based view and we need to call the as_view() method to convert it into a view function that can be used in the URL patterns.
    path('create/', invoices_views.create_invoice, name='createInvoice'),
    path('unpaid/', invoices_views.show_unpaid_invoices, name='unpaid_invoices'),
    path('mark_paid/', invoices_views.mark_as_paid, name='mark_as_paid'),
    path('one_invoice/', invoices_views.show_one_invoice, name='one_invoice'),
    path('invoice/add',invoices_views.add_invoice, name='add_invoice'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name='login'), # LoginView is a built-in class-based view provided by Django for handling user authentication. It renders a login form and processes the login request.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # LogoutView is a built-in class-based view provided by Django for handling user logout. It logs the user out and redirects them to a specified page.
    path('signup/', accounts_views.signup, name='signup'), # This line maps the URL path 'signup/' to the signup view function defined in the invoices app's views.py file. When a user visits 'http://<your-domain>/signup/', they will be directed to the signup page where they can create a new account.
]