from django import forms
from .models import Subscriber

class SubscriberPaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range (1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2038)]

    card_number = forms.CharField(label='Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)