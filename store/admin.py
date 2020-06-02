from django.contrib import admin
from .models import Store, Menu

class MenuInine(admin.TabularInline):
    model = Menu

class StoreAdmin(admin.ModelAdmin):
    inlines = [
        MenuInine,
    ]

admin.site.register(Store, StoreAdmin)
