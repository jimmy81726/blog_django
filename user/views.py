from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_register(request):
    message = ""
    if request.method == "GET":
        pass
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            if password1 != password2:
                message = "密碼不一致,請重新輸入"
            elif len(password1) < 8:
                message = "密碼長度不足至少8個字元"
            else:
                if User.objects.filter(username=username):
                    message = "帳號已存在"
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password1
                    )
                    user.save()
                    message = "註冊成功"
        except Exception as e:
            print(e)
            message = "註冊失敗"

    return render(request, "user/register.html", {"message": message})


def user_login(request):
    message = ""
    if request.method == "POST":
        if request.POST.get("register"):
            return redirect("register")
        if request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            print(user)
            if not user:
                message = "帳號或密碼錯誤,請重新輸入"
            else:
                login(request, user)
                message = "登入成功"

    return render(request, "user/login.html", locals())


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")
