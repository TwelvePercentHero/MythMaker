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
from .models import Membership

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def profile(request):
    username = request.user.username
    context = {'username' : username}
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
        return HttpResponse('Activation link is invalid!')

@login_required
def benefits(request):
    return render(request, 'registration/benefits.html')




