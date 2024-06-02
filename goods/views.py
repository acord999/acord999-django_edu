from django.shortcuts import render

from goods.models import Categories


def catalog(request):
    categories = Categories.objects.all()
    print(categories)
    context = {
        "title": "Home - Catalog",
        "goods": [],
        "catrgories": categories,
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    context = {}
    return render(request, "goods/product.html", context)
