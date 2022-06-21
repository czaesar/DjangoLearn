from operator import index
from django import views
from django.urls import path #шаг 6
from .views import *            #шаг 8


urlpatterns = [   #шаг 7
    path('', index, name = 'home'),
    path('about/', about, name='about'),
    path('news/<int:news_id>/', view_news, name = 'view_news'), # Создаем путь который по id будет переходить на новости
]

