from django import forms
from .models import Subscriber

class SubscriberForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range (1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2038)]

    card_number = forms.CharField(required=False)
    cvc = forms.CharField(required=False)
    expiry_month = forms.ChoiceField(choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)