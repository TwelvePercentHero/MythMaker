from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import stripe

class Subscriber(models.Model):
    user_rec = models.ForeignKey(User, on_delete='CASCADE')
    address_one = models.CharField(max_length=50, blank=False)
    address_two = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return u"%s's Subscription Info" % self.user_rec

