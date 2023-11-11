from django import forms
from .models import Post, Category, Comment

# 把category的資料表抓過來,[('Category1', 'Category1'), ('Category2', 'Category2')],左邊為存在數據庫的值,右邊為顯示的值
# choices = Category.objects.all().values_list("name", "name")

# # 把querylist更改成一般list
# choices_list = []
# for i in choices:
#     choices_list.append(i)


class CommentForm(forms.ModelForm):
    # 在Meta下寫是針對內部已有的更新
    class Meta:
        model = Comment
        fields = ("name", "comment_content")
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "請輸入暱稱"}
            ),
            "comment_content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入留言"}
            ),
        }
        labels = {
            "name": "暱稱",
            "comment_content": "留言",
        }


# 發布文章所用的form繼承自Post model
class PostForm(forms.ModelForm):
    # 在Meta下寫是針對內部已有的更新
    # 寫進問題討論
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="文章類型",
        empty_label="請選擇",
    )

    class Meta:
        model = Post
        fields = ("title", "author", "category", "images", "content")
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
            # "category": forms.Select(
            #     choices=choices_list, attrs={"class": "form-select"}
            # ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入內容"}
            ),
        }
        labels = {
            "title": "標題",
            "author": "作者",
            "category": "文章類型",
            "content": "內容",
            "images": "開頭圖片",
        }


# 修改文章所用的form繼承自Post model
class EditForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="文章類型",
        empty_label="請選擇",
    )

    class Meta:
        model = Post
        fields = ("title", "category", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "請輸入標題"}
            ),
            # "category": forms.Select(
            #     choices=choices_list, attrs={"class": "form-select"}
            # ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入評論"}
            ),
        }
        labels = {
            "title": "標題",
            "category": "文章類型",
            "content": "內容",
        }
