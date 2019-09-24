from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms.forms import NON_FIELD_ERRORS
from django.conf import settings
from .models import Subscriber
from .forms import SubscriberPaymentForm

import stripe

@login_required
def benefits(request):
    return render(request, 'subscription/benefits.html')

@login_required
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberPaymentForm(request.POST)
        if form.is_valid():
            fee = settings.SUBSCRIPTION_PRICE
            try:
                stripe_customer = sub.charge(request, email, fee)
            except stripe.StripeError as e:
                form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])
                return render(request, template, {'form' : form, 'STRIPE_PUBLISHABLE_KEY' : settings.STRIPE_PUBLISHABLE_KEY})
    else:
        form = SubscriberPaymentForm()
    return render(request, 'accounts/profile.html')  

