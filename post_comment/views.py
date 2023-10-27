from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class ArticleShow(ListView):
    model = Post
    template_name = "./post_comment/index.html"
    # ordering = ["-id"]


# DetailView需要傳參數
class ArticleDetailShow(DetailView):
    model = Post
    template_name = "./post_comment/article_detail.html"


class WriteAritcle(CreateView):
    model = Post
    form_class = PostForm
    template_name = "./post_comment/create_article.html"
    # 把model的所有欄位顯示
    # fields = "__all__"


class EditArticle(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "./post_comment/update_article.html"
    # fields = ["title", "content"]


class DelecteArticle(DeleteView):
    model = Post
    template_name = "./post_comment/delete_article.html"
    success_url = reverse_lazy("article-show")


@login_required
def user_post(request):
    user = request.user
    if user.is_authenticated:
        # 讓Post的author去找User里篩選
        user_posts = Post.objects.filter(author=user)

    return render(
        request, "./post_comment/user_article.html", {"user_posts": user_posts}
    )
