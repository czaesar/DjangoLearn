from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse('Hello')


def test(request):
    return HttpResponse('Тестовая страница')