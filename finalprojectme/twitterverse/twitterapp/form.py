from django import forms
from orders.models import *

class PizzaForm (forms.ModelForm):
    ''' Creates a form where users can choose toppings '''
    class Meta:
        model = Cart # Retrieves fields from Cart
        exclude = ["Items","Username","Status","Price"] #Only Toppings field id required


    def __init__ (self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)
