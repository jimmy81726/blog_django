from django.urls import path
from .views import (
    UserRegister,
    UserEditProfile,
    user_login,
    user_logout,
    change_success,
    ProfileShow,
    EditProfileCard,
    CreateProfileCard,
)
from django.contrib.auth import views as auth_views

# PasswordChange.as_view()的url在最原本的urls.py
urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("edit-profile", UserEditProfile.as_view(), name="edit-profile"),
    path("show-profile/<int:pk>", ProfileShow.as_view(), name="show-profile"),
    path(
        "edit-profilecard/<int:pk>", EditProfileCard.as_view(), name="edit-profilecard"
    ),
    path(
        "create-profilecard/",
        CreateProfileCard.as_view(),
        name="create-profilecard",
    ),
    path("change-success/", change_success, name="change-success"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # path(
    #     "password/",
    #     auth_views.PasswordChangeView.as_view(
    #         template_name="user/change_password.html"
    #     ),
    #     name="password",
    # ),
]
