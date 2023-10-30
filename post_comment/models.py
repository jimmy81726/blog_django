from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default="其他")

    def __str__(self):
        return self.title + " | " + str(self.author)

    # 按下發布導向的網頁
    def get_absolute_url(self):
        return reverse("index")
