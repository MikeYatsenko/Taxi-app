from django import forms
from django.contrib.auth.models import User
from .models import Order, Car



class OrderForm(forms.ModelForm):

    class Meta():
       model = Order
       fields = ('name', 'surname', 'phone_number','adress_from','adress_to', 'time')

