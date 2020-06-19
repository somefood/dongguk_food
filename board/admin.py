from django.contrib import admin
from .models import UserBoard


# admin.site.register(UserBoard)

@admin.register(UserBoard)
class UserBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'modified_dt')
    list_filter = ('modified_dt',)
    search_fields = ('title', 'content')