from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.views.generic import ListView
from .forms import MythMakerForm, SubscriberForm
from .tokens import account_activation_token
from .models import Membership, MythMakerMembership, Subscription

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Convenience method to get user membership
def get_user_membership(request):
    user_membership_qs = MythMakerMembership.objects.filter(user = request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

@login_required
def profile(request):
    username = request.user.username
    user_membership = get_user_membership(request)
    context = {'username' : username, 'user_membership' : user_membership}
    return render(request, 'registration/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = MythMakerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your MythMaker account'
            message = render_to_string('registration/activation_email.html', {
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'registration/activate.html')
    else:
        form = MythMakerForm()
    return render(request, 'registration/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'registration/confirmation.html')
    else:
        return render(request, 'registration/invalid_code.html')

@login_required
def benefits(request):
    username = request.user.username
    user_membership = get_user_membership(request)
    context = {'username' : username, 'user_membership' : user_membership}
    return render(request, 'registration/benefits.html', context)

@login_required
def upgrade(request):
    username = request.user.username
    user_membership = get_user_membership(request)
    publishKey = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            customer = stripe.Customer.retrieve(user_membership.stripe_customer_id)
            customer.source = token
            customer.save()
            subscription = stripe.Subscription.create(
                customer = user_membership.stripe_customer_id,
                items=[
                    {'plan': 'plan_Fxgr7BZfN3p3YR'},
                ]
            )
            return redirect(reverse('update_membership', kwargs={ 'subscription_id' : subscription.id }))
        except:
            return render(request, 'registration/card_declined.html')

    context = {'username' : username, 'publishKey' : publishKey, 'user_membership' : user_membership}
    return render(request, 'registration/upgrade.html', context)

@login_required
def updateMembership(request, subscription_id):
    username = request.user.username
    user_membership = get_user_membership(request)
    new_membership = Membership.objects.get(pk=2)
    user_membership.membership = new_membership
    user_membership.save()

    sub = Subscription.objects.get_or_create(mythmaker_membership = user_membership,
                                            stripe_subscription_id = subscription_id,
                                            active = True)

    context = {'username' : username, 'user_membership' : user_membership}

    return render(request, 'registration/profile.html', context)

    










