from django.contrib import admin
from .models import Store, Menu

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class StoreAdmin(admin.ModelAdmin):
    pass