from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django_blog.article.models import Article

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