from .models import Category


# 為了讓base.html的文章類別,總是能取到cate_list參數,setting也要做設定
def category_list(request):
    cate_list = Category.objects.all()
    return {"cate_list": cate_list}
