from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView #etc
from django.shortcuts import render # it's used to render the template with context data (variables). It takes the request object, template name, and context data as arguments and returns an HttpResponse object with the rendered template.
# Create your views here.

# Function based view
# def show_invoice(request):
#     return HttpResponse("This is the invoice page.")

# def show_invoice(request):
#     data = {
#         'invoice_number': 'INV-001',
#         'customer_name': 'John Doe',
#         'amount': 100.00,
#         'due_date': '2023-12-31'
#     }
#     return render(request, 'cusName.html', data) #(request, template_name, data to pass to template)

def show_invoice(request):
    data = {
        'all_invoices': [
            {'invoice_number': 'INV-001', 'customer_name': 'John Doe', 'amount': 100.00, 'due_date': '2023-12-31'},
            {'invoice_number': 'INV-002', 'customer_name': 'Jane Smith', 'amount': 200.00, 'due_date': '2024-01-15'},
            {'invoice_number': 'INV-003', 'customer_name': 'Alice Johnson', 'amount': 150.00, 'due_date': '2024-02-28'},
        ]
    }
    return render(request, 'cusName.html', data) #(request, template_name, data to pass to template)

# Class based view
class HomePageView(TemplateView): #Note: class name should end with "View" only.
    template_name = 'home.html' #Note: template_name should be defined in class based view to specify the template to be used for rendering the view.

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class BasePageView(TemplateView):
    template_name = 'base.html'

# Retrive Invoice model (table) from list of models for storing data.
from .models import Invoice

# Create a new record
def create_invoice(request):
    # Basically we are telling Invoice model to create a new row and store it in Invoice.
    Invoice.objects.create( # Invoice is a model, object is manager, create is a built-in function of model.
        customer_name = "Girish",
        invoice_number = "INV-005",
        amount = 10000.00,
        is_paid = True
    )
    data ={'message': 'Invoice created successfully!'}
    return render(request, 'cusName.html', data)  

# fetch record
def show_one_invoice(request):
    # invoice = Invoice.objects.get(invoice_number = 'INV-005') #get will raise error if he can't find invoice number.
    invoice = Invoice.objects.filter(invoice_number='INV-005').first() #.first() returns None instead of crashing if the record doesn't exist, and it never raises MultipleObjectsReturned.
    data = { #object
        'invoice': invoice,
        'all_invoices': [invoice]
    }
    return render(request,'cusName.html', data)

# filter record
def show_unpaid_invoices(request):
    unpaid_invoices = Invoice.objects.filter(is_paid = False)

    data = {
        'unpaid_invoices': unpaid_invoices
    }
    return render(request,'cusName.html', data)

# Update record
def mark_as_paid(request):
    Invoice.objects.filter(invoice_number = "INV-005").update(is_paid=True)

    all_invoices = Invoice.objects.filter(is_paid = False)
    data ={
        "all_invoices": all_invoices
    }
    return render(request,'cusName.html', data)

# Forms
from .forms import InvoiceForm
from django.shortcuts import redirect # redirect to different web page.

def add_invoice(request):
    if request.method == 'POST': # it checks if user has submitted the form or not. If yes, then it will process the form data.
        form = InvoiceForm(request.POST)
        if form.is_valid():
            return redirect('all_invoices')  # Redirect to the invoice list page after successful submission
    else:
        form = InvoiceForm()
    data = {
        'form': form
    }
    return render(request, 'add_invoice.html', data)