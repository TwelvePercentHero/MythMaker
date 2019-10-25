from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, UserChangeForm
from .models import MythMaker

class MythMakerForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a username', 'tabindex': '1'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email', 'tabindex': '2'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a password', 'tabindex': '3'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password', 'tabindex': '4'})

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class ExtendedAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter username'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control', 'placeholder' : 'Enter password'})

class UpdateProfile(ModelForm):
    tagline = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    profile_image = forms.ImageField(required=False)
    profile_header = forms.ImageField(required=False)

    class Meta:
        model = MythMaker
        fields = ('tagline', 'bio', 'profile_image', 'profile_header')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tagline'].widget.attrs.update({'class' : 'edit-field'})
        self.fields['bio'].widget.attrs.update({'class' : 'edit-field', 'size' : 40})
        self.fields['profile_image'].widget.attrs.update({'class' : 'upload-field'})

    def clean_edit(self):
        tagline = self.cleaned_data['tagline']
        bio = self.cleaned_data['bio']
        profile_image = self.cleaned_data['profile_image']
        profile_header = self.cleaned_data['profile_header']

        return clean_edit