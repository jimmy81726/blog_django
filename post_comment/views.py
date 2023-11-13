from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


class LeaveComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "./post_comment/create_comment.html"

    # fields = "__all__"
    # 使用此方法回傳當下特定的文章給form指定
    def form_valid(self, form):
        # 把要傳的內容給form中Comment資料表的'post_id',kwargs["pk"]獲取url中名為pk的參數
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    # 為了回到本頁,才有表單提交成立,article-detail本來就要帶個參數
    def get_success_url(self):
        return reverse_lazy("article-detail", kwargs={"pk": self.kwargs["pk"]})


# 按下like/Unlike button之後的功能
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
    return redirect("article-detail", pk=pk)


class ArticleShow(ListView):
    model = Post
    template_name = "./post_comment/index.html"
    ordering = ["-date_posted"]


# DetailView需要傳參數
class ArticleDetailShow(DetailView):
    model = Post
    template_name = "./post_comment/article_detail.html"

    # 在class-based的基礎上要回傳值的方法
    def get_context_data(self, *args, **kwards):
        post = get_object_or_404(Post, id=self.kwargs["pk"])

        post.hit += 1
        post.save()

        # 用super使用父類的get_context_data方法傳給模板
        context = super(ArticleDetailShow, self).get_context_data(*args, **kwards)
        total_likes = post.total_likes()

        liked = False
        # 用到manytomany的方法去檢察關聯性,看當下登入的人有沒有按過讚
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["liked"] = liked
        context["total_likes"] = total_likes
        return context


class WriteAritcle(CreateView):
    model = Post
    form_class = PostForm
    template_name = "./post_comment/create_article.html"
    # 把model的所有欄位顯示
    # fields = "__all__" 假如沒有form要用form.as_p一定要打這行


class EditArticle(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "./post_comment/update_article.html"
    # fields = ["title", "content"]


class DelecteArticle(DeleteView):
    model = Post
    template_name = "./post_comment/delete_article.html"
    # 刪除完重新導向index
    success_url = reverse_lazy("user-post")


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
    cated_posts = Post.objects.filter(category=cate).order_by("-date_posted")
    return render(
        request,
        "./post_comment/category_article.html",
        {"cated_posts": cated_posts, "cate": cate},
    )
