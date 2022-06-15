from django.shortcuts import render
from django.http import  HttpResponse
from .models import News #импот созданных моделей



def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

def test(request):
    return HttpResponse('Тестовая страница')