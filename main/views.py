from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {"title": "Главная страница - Home", "content": "Магазин мебели HOME"}
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": """Телефон: +7 (800) 123-45-67
                       Email: support@home.ru
                       Адрес: Москва, ул. Ленина, д. 10, оф. 101
                       Присоединяйтесь к "Home" и создавайте уют вместе с нами!""",
    }
    return render(request, "main/about.html", context=context)
