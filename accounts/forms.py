from django import forms
from django.contrib.auth.forms import UserCreationForm

class MythMakerForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'password'}))
    password2 = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control', 'type' : 'password'}))