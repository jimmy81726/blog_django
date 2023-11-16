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
from django.shortcuts import get_object_or_404


class DeletePhoto(DeleteView):
    model = Photo
    template_name = "./album/delete_photo.html"

    # 刪除完重新導向
    def get_success_url(self):
        return reverse_lazy("detail-alb", kwargs={"albumid": self.kwargs["albumid"]})


class AddPhoto(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "./album/add_photo.html"

    def form_valid(self, form):
        # 把要傳的內容給photo資料表中'p_album_id',kwargs["albumid"]獲取url中名為albumid的參數
        form.instance.p_album_id = self.kwargs["albumid"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("detail-alb", kwargs={"albumid": self.kwargs["albumid"]})


def show_photo(request, photoid=None, albumid=None):  # 顯示單張相片
    album = Album.objects.get(id=albumid)
    photo = Photo.objects.get(id=photoid)  # 取得點選的相片
    photo.p_hit += 1  # 點擊數加1
    photo.save()  # 儲存資料
    return render(request, "./album/show_photo.html", locals())


def album_show(request, albumid=None):  # 顯示相簿
    album = albumid  # 以album_id變數傳送給html
    album_object = get_object_or_404(Album, id=albumid)
    a_author_id = album_object.a_author.id if album_object.a_author else None

    photos = Photo.objects.filter(p_album_id=album).order_by(
        "-id"
    )  # 抓albumid和讀取所有albumid相同的相片
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
    success_url = reverse_lazy("user-allalb")


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
