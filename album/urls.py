from django.urls import path
from . import views


urlpatterns = [
    path("add-alb/", views.AddAlbum.as_view(), name="add-alb"),
    path("show-allalb/", views.show_allalb, name="show-allalb"),
    path("user-allalb/", views.user_album, name="user-allalb"),
    path("del-alb/<int:pk>", views.DeleteAlbum.as_view(), name="del-alb"),
    path("detail-alb/<int:albumid>", views.album_show, name="detail-alb"),
    path(
        "show-photo/<int:photoid>/<int:albumid>/", views.show_photo, name="show-photo"
    ),
    path("add-photo/", views.AddPhoto.as_view(), name="add-photo"),
    path(
        "del-photo/<int:pk>/<int:albumid>/",
        views.DeletePhoto.as_view(),
        name="del-photo",
    ),
]
