from django.contrib import admin
from .models import UserBoard


# admin.site.register(UserBoard)

@admin.register(UserBoard)
class UserBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'modified_dt', 'tag_list')
    list_filter = ('modified_dt',)
    search_fields = ('title', 'content')
    # prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())