from django.db import models

# Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)  # 這個字段建立博客作者和User模型之間的關聯

#     def __str__(self):
#         return self.title

# class Comment(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     date_commented = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Comment by {self.author.username} on {self.blog.title}'
