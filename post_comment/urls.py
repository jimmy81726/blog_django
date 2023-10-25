from django.urls import path
from . import views
from .views import (
    ArticleShow,
    ArticleDetailShow,
    WriteAritcle,
    EditArticle,
    DelecteArticle,
)

urlpatterns = [
    path("article-show/", ArticleShow.as_view(), name="article-show"),
    # views默認要用int:pk命名
    path("article-detail/<int:pk>", ArticleDetailShow.as_view(), name="article-detail"),
    path("write-article/", WriteAritcle.as_view(), name="write-article"),
    path("edit-article/<int:pk>", EditArticle.as_view(), name="edit-article"),
    path("delete-article/<int:pk>", DelecteArticle.as_view(), name="delete-article"),
]
