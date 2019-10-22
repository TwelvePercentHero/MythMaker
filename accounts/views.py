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
from django.core import mail
from django.core.paginator import Paginator
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views.generic import ListView
from django.forms import inlineformset_factory
from .forms import MythMakerForm, UpdateProfile
from .tokens import account_activation_token
from .models import MythMaker, Membership, MythMakerMembership, Subscription

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Convenience method to get user membership
def get_user_membership(request):
    user_membership_qs = MythMakerMembership.objects.filter(user = request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

# Convenience method to get user subscription
def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(mythmaker_membership = get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None

def userlist(request):
    mythmaker_list = User.objects.all().order_by('date_joined')
    mythmakers = Paginator(mythmaker_list, 3)
    grouped_mythmakers = []
    for page in mythmakers.page_range:
        page_objects = mythmakers.page(page).object_list
        grouped_mythmakers.append(page_objects)
    context = {'mythmakers' : mythmakers, 'grouped_mythmakers' : grouped_mythmakers}
    return render(request, 'registration/userlist.html', context)

def publicprofile(request, user_id):
    mythmaker_user = User.objects.get(pk = user_id)
    context = {'mythmaker_user' : mythmaker_user }
    return render(request, 'registration/publicprofile.html', context)

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
            html_message = render_to_string('registration/activation_email.html', {
                'user' : user,
                'domain' : current_site.domain,
                'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            mail.send_mail(mail_subject, plain_message, from_email, [to_email], html_message=html_message)
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
def edit(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance = request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/edit.html', args)

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
def update(request, subscription_id):
    username = request.user.username
    user_membership = get_user_membership(request)
    new_membership = Membership.objects.get(pk=2)
    user_membership.membership = new_membership
    user_membership.save()

    sub = Subscription.objects.get_or_create(mythmaker_membership = user_membership,
                                            stripe_subscription_id = subscription_id,
                                            active = True)

    context = {'username' : username, 'user_membership' : user_membership}

    return render(request, 'registration/success.html', context)

@login_required
def confirm_cancel(request):
    return render(request, 'registration/confirm_cancel.html')

@login_required
def cancel(request):
    username = request.user.username
    user_membership = get_user_membership(request)
    user_sub = get_user_subscription(request)

    sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
    sub.delete()

    user_sub.active = False
    user_sub.save()

    revert_membership = Membership.objects.get(pk=1)
    user_membership.membership = revert_membership
    user_membership.save()

    context = {'username' : username, 'user_membership' : user_membership}

    return render(request, 'registration/sorry.html', context)
    
    










