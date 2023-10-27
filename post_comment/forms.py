from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "請輸入標題"}
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "author",
                    # 讓作者欄為當下的登入者,且沒有更改必要就隱藏起來
                    "type": "hidden",
                }
            ),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入評論"}
            ),
        }
        labels = {
            "title": "標題",
            "author": "作者",
            "content": "內容",
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "請輸入標題"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入評論"}
            ),
        }
        labels = {
            "title": "標題",
            "content": "內容",
        }
