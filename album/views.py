from django.shortcuts import render
from .models import Album, Photo
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import AlbumForm, PhotoForm
from django.urls import reverse_lazy


class DeletePhoto(DeleteView):
    model = Photo
    template_name = "./album/delete_photo.html"
    # 刪除完重新導向index
    success_url = reverse_lazy("index")


class AddPhoto(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "./album/add_photo.html"


def show_photo(request, photoid=None, albumid=None):  # 顯示單張相片
    album = Album.objects.get(id=albumid)
    photo = Photo.objects.get(id=photoid)  # 取得點選的相片
    photo.p_hit += 1  # 點擊數加1
    photo.save()  # 儲存資料
    return render(request, "./album/show_photo.html", locals())


def album_show(request, albumid=None):  # 顯示相簿
    album = albumid  # 以區域變數傳送給html

    photos = Photo.objects.filter(p_album__id=album).order_by("-id")  # 讀取所有相片
    if photos:
        monophoto = photos[0]  # 第1張相片
    else:
        message = "尚未擁有圖片"

    totalphoto = len(photos)  # 相片總數
    return render(request, "./album/detail_album.html", locals())


class DeleteAlbum(DeleteView):
    model = Album
    template_name = "./album/delete_album.html"
    # 刪除完重新導向index
    success_url = reverse_lazy("index")


class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "./album/add_album.html"


@login_required
def user_album(request):
    user = request.user
    if user.is_authenticated:
        user_albums = Album.objects.filter(a_author=user).order_by("-a_date")
    total_useralbum = len(user_albums)
    photos = []
    lengths = []
    for useralbum in user_albums:
        # 為了算相簿總數而讀取,最新家的照片放最前面
        photo = Photo.objects.filter(p_album__a_title=useralbum.a_title).order_by("-id")
        lengths.append(len(photo))  # 相簿總數
        # 設定相簿預覽
        if len(photo) == 0:  # 若無相片加入空字串
            photos.append("")
        else:
            photos.append(photo[0].p_images)  # 只加入第1張相片做預覽

    return render(request, "./album/user_album.html", locals())


def show_allalb(request):
    albums = Album.objects.all().order_by("-id")
    totalalbum = len(albums)
    photos = []
    lengths = []
    for album in albums:
        # 為了算相簿總數而讀取,最新家的照片放最前面
        photo = Photo.objects.filter(p_album__a_title=album.a_title).order_by("-id")
        lengths.append(len(photo))  # 相簿總數
        # 設定相簿預覽
        if len(photo) == 0:  # 若無相片加入空字串
            photos.append("")
        else:
            photos.append(photo[0].p_images)  # 只加入第1張相片做預覽
    return render(request, "./album/all_album.html", locals())
