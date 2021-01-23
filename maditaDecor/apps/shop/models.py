from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.CharField('Описание', max_length=1000, blank=True)
    price = models.IntegerField('Цена')
    img = models.ImageField('Картинка', upload_to='gallery', blank=True)
