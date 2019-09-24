from django.contrib import admin
from .models import Subscriber

class SubscriptionAdminStacked(admin.StackedInline):
    model = Subscriber

admin.site.register(Subscriber)