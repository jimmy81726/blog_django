from django import forms
from .models import Album, Photo


class PhotoForm(forms.ModelForm):
    # 在Meta下寫是針對內部已有的更新
    class Meta:
        model = Photo
        fields = ("p_name", "p_user", "p_album", "p_images")
        widgets = {
            "p_name": forms.TextInput(attrs={"class": "form-control"}),
            "p_album": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "p_album",
                    # 讓作者欄為當下的登入者,且沒有更改必要就隱藏起來
                    "type": "hidden",
                }
            ),
            "p_user": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "p_user",
                    # 讓作者欄為當下的登入者,且沒有更改必要就隱藏起來
                    "type": "hidden",
                }
            ),
        }
        labels = {
            "p_name": "相片名稱",
            "p_images": "圖片",
        }


class AlbumForm(forms.ModelForm):
    # 在Meta下寫是針對內部已有的更新
    class Meta:
        model = Album
        fields = ("a_title", "a_author", "a_location", "a_text")
        widgets = {
            "a_title": forms.TextInput(attrs={"class": "form-control"}),
            "a_location": forms.TextInput(attrs={"class": "form-control"}),
            "a_text": forms.Textarea(attrs={"class": "form-control"}),
            "a_author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "value": "",
                    "id": "a_author",
                    # 讓作者欄為當下的登入者,且沒有更改必要就隱藏起來
                    "type": "hidden",
                }
            ),
        }
        labels = {
            "a_title": "相簿名稱",
            "a_location": "拍攝地點",
            "a_text": "相簿說明",
        }
