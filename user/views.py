from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html", {"str": "這裡準備當首頁"})
