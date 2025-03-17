from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'address', 'payment_method']
        widgets = {
            'payment_method': forms.RadioSelect(choices=Order.PAYMENT_CHOICES)
        }