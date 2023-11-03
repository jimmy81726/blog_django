from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from post_comment.models import ProfileCard
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import Registerform, EditProfileform, PasswordChange
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import EditProfileCardform


class CreateProfileCard(generic.CreateView):
    model = ProfileCard
    template_name = "user/create_profilecard.html"
    form_class = EditProfileCardform

    # 使用此方法回傳當下的user給form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileCard(generic.UpdateView):
    model = ProfileCard
    template_name = "user/edit_profilecard.html"
    form_class = EditProfileCardform
    success_url = reverse_lazy("index")


class ProfileShow(generic.DetailView):
    model = ProfileCard
    template_name = "user/profile.html"

    def get_context_data(self, *args, **kwards):
        # 抓到特定的profile
        user_profile = get_object_or_404(ProfileCard, id=self.kwargs["pk"])
        # 把父類的參數抓下來
        context = super(ProfileShow, self).get_context_data(*args, **kwards)
        context["user_profile"] = user_profile
        return context


# 只為了跳轉該網頁
def change_success(request):
    return render(
        request,
        "user/change_success.html",
    )


# 直接用auth_views.PasswordChangeView沒辦法用success_url
class PasswordChange(PasswordChangeView):
    # form_class = PasswordChange    自己寫的form
    form_class = PasswordChangeForm
    template_name = "user/change_password.html"
    success_url = reverse_lazy("change-success")


# UpdateView更改已有對象
class UserEditProfile(generic.UpdateView):
    form_class = EditProfileform
    template_name = "user/edit_profile.html"
    success_url = reverse_lazy("index")

    # 用此方法抓自己的檔案
    def get_object(self):
        return self.request.user


# CreateView建立新對象
class UserRegister(generic.CreateView):
    form_class = Registerform
    template_name = "user/register.html"
    success_url = reverse_lazy("login")


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")


def user_login(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")
        if request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                message = "帳號或密碼錯誤,請重新輸入"
            else:
                login(request, user)
                message = "登入成功"
                # url在不同專案的寫法,urls.py也要寫好
                return redirect("index")

    return render(request, "user/login.html", locals())


# def user_register(request):
#     message = ""
#     if request.method == "GET":
#         pass
#     if request.method == "POST":
#         try:
#             username = request.POST.get("username")
#             email = request.POST.get("email")
#             password1 = request.POST.get("password1")
#             password2 = request.POST.get("password2")
#             if password1 != password2:
#                 message = "密碼不一致,請重新輸入"
#             elif len(password1) < 8:
#                 message = "密碼長度不足至少8個字元"
#             else:
#                 if User.objects.filter(username=username):
#                     message = "帳號已存在"
#                 else:
#                     user = User.objects.create_user(
#                         username=username, email=email, password=password1
#                     )
#                     user.save()
#                     message = "註冊成功"
#         except Exception as e:
#             print(e)
#             message = "註冊失敗"
#     return render(request, "user/register.html", {"message": message})


# @login_required
# def user_profile(request, id):
#     user = User.objects.get(pk=id)
#     return render(request, "user/profile.html", {"user": user})
