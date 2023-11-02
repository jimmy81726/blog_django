from typing import Any
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth.models import User
from django import forms


class EditProfileform(UserChangeForm):
    # 在Meta外寫是另外建立新的,或是同名會覆蓋掉內部的field,這邊是要做edit功能所以要確認field名要相同才覆蓋,可以去form.as_p去顯示看name的名稱
    email = forms.EmailField(
        label="更改電子郵件",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    username = forms.CharField(
        label="更變帳號名",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    last_login = forms.CharField(
        label="最後登入時間",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    date_joined = forms.CharField(
        label="註冊時間",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = ("username", "password", "email", "last_login", "date_joined")


class Registerform(UserCreationForm):
    # 在UserCreationForm的基礎上新增這些欄位,新增的widget要馬上寫在()內不另外寫
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "請輸入信箱"}
        ),
    )
    username = forms.CharField(
        label="用戶名稱",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "請輸入名稱"}),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # 基於UserCreationForm此父類別的特性要這樣修,更改內建field
    def __init__(self, *args, **kwargs):
        super(Registerform, self).__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


# 也可用自己寫的改密碼form
class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"})
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
