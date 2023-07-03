from django import forms
from django.db.models import fields
from django.forms import DateInput, PasswordInput, TextInput, widgets
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget = TextInput(attrs={'class': 'input'})
            self.fields['password'].widget = PasswordInput(attrs={'class': 'input'})
    class Meta:
        model = User
        fields = ('username', 'password')