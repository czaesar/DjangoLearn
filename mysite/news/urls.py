from operator import index
from django.urls import path #шаг 6
from .views import *            #шаг 8


urlpatterns = [   #шаг 7
    path('', index),
    path('test/', test), #шаг 9
]