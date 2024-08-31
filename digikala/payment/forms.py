from django import forms
from .models import Payment


class PaymentForm(forms.ModelForm):
    amount = forms.DecimalField(label="", max_digits=10, decimal_places=2)
    widget = forms.NumberInput(attrs={'class': 'form-control'})

    class Meta:
        model = Payment
        fields = ['amount']