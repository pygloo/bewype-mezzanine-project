# django import
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# mezzanine import
from mezzanine.core.admin import DynamicInlineAdmin
from mezzanine.core.forms import DynamicInlineAdminForm

# userena import
from userena.admin import UserenaAdmin
from userena.models import UserenaSignup


class _StackedInline(admin.StackedInline):

    template = "admin/includes/stacked.html"


class _UserenaSignupInline(_StackedInline):
    model = UserenaSignup
    max_num = 1


class _UserenaAdmin(UserAdmin):
    inlines = [_UserenaSignupInline, ]
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'date_joined')

admin.site.unregister(User)
admin.site.register(User, _UserenaAdmin)
