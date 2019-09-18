from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import MythMaker

class MythMakerInline(admin.StackedInline):
    model = MythMaker
    can_delete = False
    verbose_name_plural = 'MythMakers'

class UserAdmin(BaseUserAdmin):
    inlines = (MythMakerInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
