from django.db import models

# Create your models here.
class Invoice(models.Model): # Invoice (child class) inherits all those built-in functions from Model (parent class). This is called inheritance.
    # fields (columns)
    customer_name = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2) # decimal field with 2 decimals on right.
    date_created = models.DateField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self): #special method that returns a string
        return self.invoice_number # we return this field because, it's going represent complete row from database on admin panel.