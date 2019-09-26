from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

MEMBERSHIP_CHOICES = (
    ('Free', 'free'),
    ('Premium', 'prem')
)

class MythMaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tagline = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Membership(models.Model):
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=7)
    price = models.IntegerField(default=0)
    stripe_plan_id = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'

    def __str__(self):
        return self.membership_type

class MythMakerMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'MythMaker Membership'
        verbose_name_plural = 'MythMaker Memberships'

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    mythmaker_membership = models.ForeignKey(MythMakerMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.user_membership.user.username
