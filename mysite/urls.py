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
from invoices import views # importing views from invoices app

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
    path('cus_name/', views.show_invoice, name='cus_name'),
    # Note: you don't have to use () after show_invoice because django will do it internally when the URL is accessed.
    path('', views.LandingPageView.as_view(), name='landing'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('base/', views.BasePageView.as_view(), name='base'),
    # Note: you have to use .as_view() after class based view and we need to call the as_view() method to convert it into a view function that can be used in the URL patterns.
    path('create/', views.create_invoice, name='createInvoice'),
    path('unpaid/', views.show_unpaid_invoices, name='unpaid_invoices'),
    path('mark_paid/', views.mark_as_paid, name='mark_as_paid'),
    path('one_invoice/', views.show_one_invoice, name='one_invoice'),
    path('invoice/add',views.add_invoice, name='add_invoice'),
]