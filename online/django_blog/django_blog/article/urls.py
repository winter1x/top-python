from django.urls import path
from django_blog.article import views
from django_blog.article.views import IndexView
#from .views import IndexView

urlpatterns = [
    path("<str:tags>/<int:article_id>", views.index, name="article"),
    path("", IndexView.as_view(), name="index"),
]