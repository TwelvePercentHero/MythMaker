from django.contrib import admin
from .models import Subscription

class SubscriptionAdminStacked(admin.StackedInline):
    model = Subscription

admin.site.register(Subscription)