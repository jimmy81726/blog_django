from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Album(models.Model):
    a_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    a_title = models.CharField(max_length=255, null=False)
    a_date = models.DateTimeField(auto_now_add=True)
    a_location = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )
    a_text = models.TextField(blank=True, default="")

    def __str__(self):
        return self.a_title + " | " + str(self.a_author)

    def get_absolute_url(self):
        return reverse("show-allalb")


class Photo(models.Model):
    p_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    p_album = models.ForeignKey(
        "Album", on_delete=models.CASCADE, related_name="photos"
    )
    p_name = models.CharField(max_length=255, null=False)
    p_date = models.DateTimeField(auto_now_add=True)
    p_images = models.ImageField(null=True, blank=True, upload_to="images/")
    p_hit = models.IntegerField(default=0)

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):
        return reverse("show-allalb")
