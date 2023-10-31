from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def like_article(request, pk):
    # 獲取form表單的button name為post_id
    post_id = request.POST.get("post_id")
    # 類似fliter只是找不到會顯示error404,且只能查找單一對象
    post = get_object_or_404(Post, id=post_id)
    # post的like與User利用add建立關聯,有點過就刪除,沒點過+1
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked = True

    # 改變導入網址
    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))


class ArticleShow(ListView):
    model = Post
    template_name = "./post_comment/index.html"
    ordering = ["-date_posted"]


# DetailView需要傳參數
class ArticleDetailShow(DetailView):
    model = Post
    template_name = "./post_comment/article_detail.html"

    # 在class-based的基礎上要回傳值的方法def get_context_data,型態為QuerySet
    def get_context_data(self, *args, **kwards):
        postlike = get_object_or_404(Post, id=self.kwargs["pk"])
        # 把父類的參數抓下來
        context = super(ArticleDetailShow, self).get_context_data(*args, **kwards)
        total_likes = postlike.total_likes()

        liked = False
        # 用到manytomany的方法去檢察關聯性
        if postlike.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["liked"] = liked
        context["total_likes"] = total_likes
        return context


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
    # 刪除完重新導向index
    success_url = reverse_lazy("index")


@login_required
def user_post(request):
    user = request.user
    if user.is_authenticated:
        # 讓Post的author去利用request.user篩選
        user_posts = Post.objects.filter(author=user).order_by("-date_posted")

    return render(
        request, "./post_comment/user_article.html", {"user_posts": user_posts}
    )


# 同類的文章顯示
def category_article(request, cate):
    # 選出Post資料表中category為cate的所有文章
    cated_posts = Post.objects.filter(category=cate)
    return render(
        request,
        "./post_comment/category_article.html",
        {"cated_posts": cated_posts, "cate": cate},
    )
