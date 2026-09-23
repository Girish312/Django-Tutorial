from django.contrib import admin
from .models import Invoice #import Invoice model and fullstop is for telling model file is right here in this directory.
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin): # Custome Admin
    # This are class attributes that will be used to customize the admin interface for the Invoice model.
    # Django looks for these specific variable names to build the dashboard and The strings inside the list must match the actual field names defined in database Model.
    list_display = ['customer_name', 'invoice_number', 'amount', 'is_paid', 'date_created']
    search_fields = ['customer_name', 'invoice_number']
    list_filter = ['is_paid', 'date_created']
    ordering = ['date_created']

# admin.site is django's own admin panel and we are telling it to create a management panel for this model.
# admin.site.register(Invoice)
admin.site.register(Invoice, InvoiceAdmin) # Register the Invoice model with the custom InvoiceAdmin class to customize its admin interface.

admin.site.site_header = "Invoice Management System" # Customizing the header of the admin site.