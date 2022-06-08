from dataclasses import fields
from pyexpat import model
from django import forms
from freshman.auth.forms import UserCreationForm, UsernameField
from sales.models import Sale


class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            'first_name',
            'last_name',
            'age',
            'person',
        )

class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)



