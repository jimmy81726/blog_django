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
    path("", ArticleShow.as_view(), name="index"),
    # views默認要用int:pk命名
    path("article-detail/<int:pk>", ArticleDetailShow.as_view(), name="article-detail"),
    path("write-article/", WriteAritcle.as_view(), name="write-article"),
    path("edit-article/<int:pk>", EditArticle.as_view(), name="edit-article"),
    path("delete-article/<int:pk>", DelecteArticle.as_view(), name="delete-article"),
    path("user-post/", views.user_post, name="user-post"),
    path(
        "category-article/<str:cate>", views.category_article, name="category-article"
    ),
]
