from django.db import models
from django.db.models.signals import post_save
from django import forms
from django.contrib.auth.models import User
from django.conf import settings

from video.models import Video

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class MythMaker(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    tagline = models.TextField(max_length = 100, blank = True)
    bio = models.TextField(max_length = 500, blank = True)
    profile_image = models.ImageField(upload_to = 'profile_images', blank = True)
    profile_header = models.ImageField(upload_to = 'profile_headers', blank = True)

    class Meta:
        verbose_name = 'MythMaker'
        verbose_name_plural = 'MythMakers'

    def __str__(self):
        return 'MythMaker'

def create_mythmaker(sender, instance, created, *args, **kwargs):
    if created:
        MythMaker.objects.create(user = instance)

post_save.connect(create_mythmaker, sender = User)

class Membership(models.Model):
    FREE = 'FR'
    PREMIUM = 'PR'
    MEMBERSHIP_CHOICES = [
        (FREE, 'Free'),
        (PREMIUM, 'Premium'),
    ]
    membership_type = models.CharField(choices = MEMBERSHIP_CHOICES, blank = False, max_length = 2)
    price = models.IntegerField(default = 0)
    stripe_plan_id = models.CharField(max_length = 40)

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'

    def __str__(self):
        return self.membership_type

DEFAULT_MEMBERSHIP_ID = 1

class MythMakerMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    stripe_customer_id = models.CharField(max_length = 40)
    membership = models.ForeignKey(Membership, on_delete = models.SET_NULL, null = True, default = DEFAULT_MEMBERSHIP_ID)

    class Meta:
        verbose_name = 'MythMaker Membership'
        verbose_name_plural = 'MythMaker Memberships'

    def __str__(self):
        return self.user.username

def post_save_mythmaker_membership_create(sender, instance, created, *args, **kwargs):
    if created:
        MythMakerMembership.objects.get_or_create(user = instance)

    mythmaker_membership, created = MythMakerMembership.objects.get_or_create(user = instance)

    if mythmaker_membership.stripe_customer_id is None or mythmaker_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email = instance.email)
        mythmaker_membership.stripe_customer_id = new_customer_id['id']
        mythmaker_membership.save()

post_save.connect(post_save_mythmaker_membership_create, sender = settings.AUTH_USER_MODEL)

class Subscription(models.Model):
    mythmaker_membership = models.ForeignKey(MythMakerMembership, on_delete = models.CASCADE)
    stripe_subscription_id = models.CharField(max_length = 40)
    active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.mythmaker_membership.user.username
