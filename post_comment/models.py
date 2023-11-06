from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Comment(models.Model):
    # class "Comment"等等用comments來代替
    # 建立連結,每個post建立相對應的comment,""避免循環導入問題
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment_content = models.TextField()
    comment_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " | " + str(self.name)


class ProfileCard(models.Model):
    # 先建立與User的連結,連到外鍵author
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    selfinfo = models.TextField()
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    ig_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profilecard"
    )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("index")


# 只是建立類別名,以供文章發布和修改用,只可由超級使用者在admin增加修改
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # 按下發布導向的網頁
    def get_absolute_url(self):
        return reverse("index")


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 圖片上傳至images/
    images = models.ImageField(null=True, blank=True, upload_to="images/")
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="其他")
    # 讓likes與User做關聯,利用related_name反向查詢
    likes = models.ManyToManyField(User, related_name="blog_posts")

    # 定義一個處理likes的方法
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    # 按下發布導向的網頁
    def get_absolute_url(self):
        return reverse("index")
