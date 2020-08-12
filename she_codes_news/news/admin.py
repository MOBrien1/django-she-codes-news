from django.contrib import admin
from .models import NewsStory, Comment


# Register your models here.


admin.site.register(NewsStory)
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment_text', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'comment_text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)