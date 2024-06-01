from django.urls import path
from goods import views


# Пространство имен
app_name = "goods"

urlpatterns = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
