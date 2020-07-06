from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']+=('nickname', 'phone_number')
    UserAdmin.add_fieldsets += (
        (('Additional Info'),{'fields':('nickname','phone_number')}),
    )
admin.site.register(User, CustomUserAdmin)