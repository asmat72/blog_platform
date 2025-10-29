from django.contrib import admin
from .models import Post, Comment, Tag, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content')
    search_fields = ('author', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag)
admin.site.register(Like)
