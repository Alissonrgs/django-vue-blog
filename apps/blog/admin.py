from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ('author', 'description', 'liked', 'status', 'posted')
    list_display = ('author', 'description', 'status', 'posted')
    search_fields = ('author__username', 'description')
    list_filter = ('status', 'posted')


class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'author', 'description', 'liked', 'status', 'posted')
    list_display = ('author', 'post', 'description', 'status', 'posted')
    search_fields = ('author__username', 'description')
    list_filter = ('status', 'posted')
    raw_id_fields = ('post',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
