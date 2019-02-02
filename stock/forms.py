from django import forms
from .models import Supply


class RestockForm(forms.Form):
    name = forms.CharField(max_length="30")
    quantity = forms.IntegerField(min_value=0)
    unit_price = forms.DecimalField(max_digits=11, decimal_places=2)
    new_quantity = forms.IntegerField(min_value=0)
    new_price = forms.DecimalField(max_digits=11, decimal_places=2)
