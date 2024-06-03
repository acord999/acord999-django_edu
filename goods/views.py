from django.shortcuts import render


from goods.models import Categories, Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        "title": "Home - Catalog",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {}
    return render(request, "goods/product.html", context)
