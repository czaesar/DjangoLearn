from distutils.command.upload import upload
from django.db import models

class News(models.Model): #шаг 9
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)#blank не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True) #дата и время создания новости
    updated_at = models.DateTimeField(auto_now=True)#Время и дата обновления новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')#позволяет загружать изображения, upload_to позволяет выбирать куда именно загружать файл /%Y -год /%m -месяц позволяет поструктурно загружать фотки
    is_published = models.BooleanField(default=True)#новость по умолчанию публикуется 
