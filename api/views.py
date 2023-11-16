from django.shortcuts import render
from post_comment.models import Post
from django.http import HttpResponse
from datetime import datetime
import json
from django.contrib.auth.models import User

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     # 圖片上傳至images/
#     images = models.ImageField(null=True, blank=True, upload_to="images/")
#     content = RichTextField(blank=True, null=True)
#     # content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#     category = models.CharField(max_length=255, default="其他")
#     # 讓likes與User做關聯,利用related_name反向查詢
#     likes = models.ManyToManyField(User, related_name="blog_posts")
#     hit = models.IntegerField(default=0)


# 取得所有post
def post_api(request):
    posts = Post.objects.all()
    post_list = []
    try:
        for post in posts:
            post_data = {
                "id": post.id,
                "title": post.title,
                "author": post.author.username,
                "content": post.content,
                "date_posted": post.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
                "category": post.category,
                "comments": [
                    # 利用related_name反向查詢
                    {"comment": comment.comment_content}
                    for comment in post.comments.all()
                ],
                "hit": post.hit,
            }
            post_list.append(post_data)
    except Exception as e:
        print(e)

    post_list = json.dumps(post_list, ensure_ascii=False)
    return HttpResponse(post_list, content_type="application/json")


# 取得單一使用者的全部文章資訊
def user_post_api(request, id):
    post_list = []
    result = "success"
    user = None
    try:
        user = User.objects.get(pk=id)
        posts = Post.objects.filter(author=user)
        for post in posts:
            post_data = {
                "id": post.id,
                "title": post.title,
                "author": post.author.username,
                "content": post.content,
                "date_posted": post.date_posted.strftime("%Y-%m-%d %H:%M:%S"),
                "category": post.category,
                "comments": [
                    # 利用related_name反向查詢
                    {"comment": comment.comment_content}
                    for comment in post.comments.all()
                ],
                "hit": post.hit,
            }

            post_list.append(post_data)

        user = user.username
    except Exception as e:
        print(e)
        result = "error"

    # 包裝再包裝,使檢視清楚
    json_data = json.dumps(
        {"result": result, "user": user, "data": post_list}, ensure_ascii=False
    )

    return HttpResponse(json_data, content_type="application/json")
