from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm
from django.conf import settings
from django.utils import timezone
import stripe

def benefits(request):
    return render(request, 'subscription/benefits.html')

@login_required()
def subscribe(request):
    if request.method == 'POST':
        subscription_form = MakePaymentForm(request.POST)

        if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)
            subscription_date = timezone.now()
            subscription.save

