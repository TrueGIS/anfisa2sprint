from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
    ice_cream_list = IceCream.objects.values('id', 'title', 'category__title')
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template, context)
