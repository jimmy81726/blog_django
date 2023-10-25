from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post


class ArticleShow(ListView):
    model = Post
    template_name = "./post_comment/articlepage.html"


class ArticleDetailShow(DetailView):
    model = Post
    template_name = "./post_comment/article_detail.html"


@login_required
def create_article(request, id):
    user = User.objects.get(pk=id)
    message = "Hello article"
    return render(request, "./post_comment/create_article.html", locals())
