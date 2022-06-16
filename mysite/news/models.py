from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from unicodedata import category
from django.db import models

class News(models.Model): #шаг 9
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')#blank не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата Публикации') #дата и время создания новости
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')#Время и дата обновления новости
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank = True)#позволяет загружать изображения, upload_to позволяет выбирать куда именно загружать файл /%Y -год /%m -месяц позволяет поструктурно загружать фотки
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')#новость по умолчанию публикуется 
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null = True, verbose_name='Категория')
    

    def __str__(self): #При вызове  News.objects.all() в shell консоли title будет выводится таким каким мы его задавали в переменной News1,News2 и т.д.
        return self.title

    class Meta:
        verbose_name = 'Новость ' #изменения в админке
        verbose_name_plural = 'Новости' #во множественом числе
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категорий')


    def __str__(self):
        return self.title

    class Meta:
      verbose_name = 'Категория ' 
      verbose_name_plural = 'Категории' 
      ordering = ['title']