from django.shortcuts import render
from django.http import  HttpResponse
from .models import News #импот созданных моделей



def index(request):
    news = News.objects.all()
    context = {
    'news': news, 
    'title': 'Список новостей'}

    return render(request, 'news/index.html', {'news': news, 'title': 'Главная страница'})


def about(request):
    return render(request, 'news/about.html', {'title': 'О сайте'})



def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})



def contacts(request):
    return render(request, 'news/contacts.html', {'title': 'Контакты'})