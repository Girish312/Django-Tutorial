from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta: # This class tells ModelForm which database model to use (Invoice), which specific data fields to include, and how to style the HTML input elements using custom widgets.
        model = Invoice
        fields = ['customer_name', 'invoice_number', 'amount', 'is_paid']  # Specify the fields to include in the form
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount < 0:
            raise forms.ValidationError("Amount should be greater than 0.")
        return amount