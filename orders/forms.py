from django import forms
from .models import Order



class OrderCreateForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()
    postal_code = forms.CharField()
    city = forms.CharField()


# class OrderCreateForm(forms.ModelForm):
#     pass
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'email', 'address',
#                   'postal_code', 'city']
