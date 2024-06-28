from django.db import models


class StaticPages(models.Model):
    title = models.CharField('Название страницы', max_length=100)
    description = models.CharField('Описание страницы', max_length=200)
    content = models.TextField('Содержимое страницы', max_length=1000)
    avatar = models.ImageField(upload_to='static_pages/', blank=True)
