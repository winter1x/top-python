from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django_blog.article.models import Article, Comment, BlogUser
from django_blog.article.forms import ArticleCommentForm

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

class CommentCreateView(View):
    # def post(self, request, *args, **kwargs):
    #     article = get_object_or_404(Article, id=kwargs['article_id'])
    #     form = ArticleCommentForm(request.POST)

    #     if form.is_valid():
    #         Comment.objects.create(
    #             text=form.cleaned_data["text"],
    #             article=article,
    #             author=request.user
    #         )
    #         return redirect('article_comments', article_id=article.id)

    #     return render(
    #         request,
    #         "articles/create.html",
    #         context={
    #             "article": article,
    #             "form": form
    #         },
    #     )

    # def get(self, request, *args, **kwargs):
    #     article = get_object_or_404(Article, id=kwargs['article_id'])
    #     form = ArticleCommentForm()
    #     return render(request, "articles/comments.html", context={"article": article, "form": form})

    def post(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.text = check_for_spam(form.cleaned_data["text"])
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('article_comments', article_id=article.id)
        return render(request, "articles/create.html", context={"form": form, "article": article})

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        form = ArticleCommentForm()
        return render(request, "articles/create.html", context={"form": form, "article": article})