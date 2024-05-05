"""Модели связанные с пользователем"""

from django.db import models
from django.contrib.auth.models import AbstractUser

EMAIL_LENGTH = 254
NAMES_LENGTH = 100


class Country(models.Model):
    """Класс Стран"""
    name_ru = models.CharField(
        'Название Русское',
        max_length=NAMES_LENGTH,
        blank=False,
        unique=True
    )
    name_en = models.CharField(
        'Название Английское',
        max_length=NAMES_LENGTH,
        blank=False,
        unique=True
    )

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ('name_ru',)

    def __str__(self) -> str:
        return f'{self.name_ru}'


class City(models.Model):
    """Класс городов"""
    name_ru = models.CharField(
        'Название Русское',
        max_length=NAMES_LENGTH,
        blank=False
    )
    name_en = models.CharField(
        'Название Английское',
        max_length=NAMES_LENGTH,
        blank=False
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name='Город'
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name_ru',)

    def __str__(self) -> str:
        return f'{self.country.name_ru} - {self.name_ru}'


class User(AbstractUser):
    """Класс описания пользователя"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    email = models.EmailField(
        'Электронная почта',
        max_length=EMAIL_LENGTH,
        unique=True
    )
    first_name = models.CharField('Имя', max_length=NAMES_LENGTH, blank=False)
    last_name = models.CharField(
        'Фамилия',
        max_length=NAMES_LENGTH,
        blank=False
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=11,
        blank=True
    )
