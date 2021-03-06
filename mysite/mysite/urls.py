"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings 
from django.conf.urls.static import static #возможно эту дичь вручную писать над будет
from django.contrib import admin
from django.urls import path, include #шаг 4 импорт include для того чтобы подключать другие urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')) #шаг 8, создаем пустую строку, чтобы показывало главную страницу без префиксов

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Формируем этот маршрут только в отладочном режиме