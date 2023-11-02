from django import forms
from .models import Post, Category

# 把category的資料表抓過來,[('Category1', 'Category1'), ('Category2', 'Category2')],左邊為存在數據庫的值,右邊為顯示的值
choices = Category.objects.all().values_list("name", "name")

# 把querylist更改成一般list
choices_list = []
for i in choices:
    choices_list.append(i)


# 發布文章所用的form繼承自Post model
class PostForm(forms.ModelForm):
    # 在Meta下寫是針對內部已有的更新
    class Meta:
        model = Post
        fields = ("title", "author", "category", "content")
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
            "category": forms.Select(
                choices=choices_list, attrs={"class": "form-select"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入評論"}
            ),
        }
        labels = {
            "title": "標題",
            "author": "作者",
            "category": "文章類型",
            "content": "內容",
        }


# 修改文章所用的form繼承自Post model
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "category", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "請輸入標題"}
            ),
            "category": forms.Select(
                choices=choices_list, attrs={"class": "form-select"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "請輸入評論"}
            ),
        }
        labels = {
            "title": "標題",
            "category": "文章類型",
            "content": "內容",
        }
