from django.contrib import admin
from .models import UserBoard, Comment


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(UserBoard)
class UserBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'modified_dt', 'tag_list')
    list_filter = ('modified_dt',)
    search_fields = ('title', 'content')
    inlines = [
        CommentInline,
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())