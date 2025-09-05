from django.urls import path
from django_blog.article import views
from django_blog.article.views import IndexView, ArticleView, ArticleCommentView, CommentCreateView, CommentEditView

urlpatterns = [
    path("<str:tags>/<int:article_id>", views.index, name="article"),
    path("", IndexView.as_view(), name="article_index"),
    path("<int:id>/", ArticleView.as_view(), name="article_view"),
    path("<int:article_id>/comments/", ArticleCommentView.as_view(), name="article_comments"),
    path("<int:article_id>/comments/create/", CommentCreateView.as_view(), name="comment_create"),
    path("<int:article_id>/comments/<int:comment_id>/edit/", CommentEditView.as_view(), name="comment_edit"),
]