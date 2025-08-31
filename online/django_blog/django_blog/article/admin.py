from django.contrib import admin
from .models import Article, Comment
from django.contrib.admin import DateFieldListFilter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
    )
    search_fields = ['name', 'body']
    list_filter = (
        ('created_at', DateFieldListFilter),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        'article',
        'text',
        "created_at",
    )
    search_fields = ['author__username', 'text']
    list_filter = (
        ('created_at', DateFieldListFilter),
    )

