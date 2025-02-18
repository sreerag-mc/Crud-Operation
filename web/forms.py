from .models import User
from django . core import validators
from django import forms



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']