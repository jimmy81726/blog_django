from django.shortcuts import render


# Create your views here.
def index(request):
    message = "這是首頁"
    return render(request, "index.html", locals())
