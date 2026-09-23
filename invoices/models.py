from django.db import models

# Create your models here.
class Invoice(models.Model): # Model is a class which has some built-in functions, and Invoice become a child class.
    # fields (columns)
    customer_name = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2) # decimal field with 2 decimals on right.
    date_created = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self): #special method that returns a string
        return self.invoice_number # we return this field because, it's going represent complete row from database on admin panel.