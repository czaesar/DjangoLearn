from operator import index
from django.urls import path #шаг 6
from .views import *            #шаг 8


urlpatterns = [   #шаг 7
    path('', index, name = 'home'),
    path('about/', about, name='about')
   
]