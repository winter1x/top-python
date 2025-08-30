from django.urls import path
from django_blog.article import views
from django_blog.article.views import IndexView, ArticleView #, ArticleCommentsView
#from .views import IndexView

urlpatterns = [
    path("<str:tags>/<int:article_id>", views.index, name="article"),
    path("", IndexView.as_view(), name="article_index"),
    path("<int:id>/", ArticleView.as_view(), name="article_view"),
]

# urlpatterns += [
#     path('<int:article_id>/comments/<int:id>', ArticleCommentsView.as_view(), name='article_comments'),
# ]