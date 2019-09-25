from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import SubscriberForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def benefits(request):
    return render(request, 'subscription/benefits.html')

@login_required
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscribe = form.save(commit=False)
            subscribe.date = timezone.now()
            subscribe.save()

            try:
                customer = stripe.Charge.create(
                    amount = settings.SUBSCRIPTION_PRICE,
                    currency = "GBP",
                    description = request.user.email,
                    card = form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined.')

            if customer.paid:
                messages.error(request, 'You have successfully paid.')
                return redirect(reverse('profile'))
            else:
                messages.error(request, 'Unable to take payment.')
        
        else:
            print(form.errors)
            messages.error(request, 'We were unable to take payment with that card.')
    else:
        form = SubscriberForm()
    return render(request, 'subscription/upgrade.html', {"form" : form, 'publishable' : settings.STRIPE_PUBLISHABLE_KEY})  

