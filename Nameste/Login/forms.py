from django import forms
from .models import *


class RegisterForm(forms.Form):
    firstname = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'id': 'names', 'placeholder': 'First Name'}))
    lastname = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'id': 'names', 'placeholder': 'Last Name'}))
    email = forms.EmailField(
        max_length=100, widget=forms.TextInput(attrs={'id': 'logininputs', 'placeholder': 'Email'}))
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'id': 'logininputs', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=50,
                               widget=forms.PasswordInput(attrs={'id': 'logininputs', 'placeholder': 'Password'}))
    conformpassword = forms.CharField(max_length=50,
                                      widget=forms.PasswordInput(attrs={'id': 'logininputs', 'placeholder': 'Conform Password'}))
    address = forms.CharField(max_length=80, widget=forms.TextInput(
        attrs={'id': 'logininputs', 'placeholder': 'Address Line'}))
    streetno = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'names', 'placeholder': 'Street No'}))
    postalcode = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'names', 'placeholder': 'Street No'}))
