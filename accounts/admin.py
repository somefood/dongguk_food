from django.contrib import admin
# from .models import Profile
#
# class AccountsAdmin(admin.ModelAdmin):
#     list_display = ('nickname',)
#
# admin.site.register(Profile, AccountsAdmin)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)