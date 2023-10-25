from django.urls import path
from . import views
from .views import ArticleShow, ArticleDetailShow

urlpatterns = [
    path("create-article/<int:id>", views.create_article, name="create-article"),
    path("article-show", ArticleShow.as_view(), name="article-show"),
    # views默認要用int:pk命名
    path("article-detail/<int:pk>", ArticleDetailShow.as_view(), name="article-detail"),
]
