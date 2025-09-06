from django.db import models
from django_blog.users.models import BlogUser
from django.contrib.auth import get_user_model

class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    title = models.CharField('title', max_length=100, blank=False)
    text = models.CharField("text", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author} к статье {self.article.name}"