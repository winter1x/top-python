from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django_blog.article.models import Article, Comment

def index(request, tags, article_id):
    return HttpResponse(f'Статья {article_id} с тегом {tags}')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles
            },
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article
            },
        )

class ArticleCommentView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        comments = Comment.objects.filter(article__id=kwargs['article_id'])
        return render(
            request,
            "articles/comments.html",
            context={
                "article": article,
                "comments": comments
            },
        )