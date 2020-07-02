from django.contrib import admin
from .models import Store, Menu

class MenuInine(admin.TabularInline):
    model = Menu


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    # list_display = ('name', 'slug', 'location', 'phone_number', 'description', 'store_image', 'likes', 'tag_list')
    list_display = ('name', 'slug', 'location', 'phone_number', 'description', 'store_image', 'tag_list')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        MenuInine,
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())