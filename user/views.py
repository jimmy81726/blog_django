from django.shortcuts import render
from django.contrib.auth.models import User


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
