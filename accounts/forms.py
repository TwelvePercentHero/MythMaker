from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

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

class SubscriberForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range (1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2039)]

    card_number = forms.CharField(required=False)
    cvc = forms.CharField(required=False)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)