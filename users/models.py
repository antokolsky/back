"""Модели связанные с пользователем"""

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from countries.models import Country

from projects.models import ProjectAttribute, Style, Material

EMAIL_LENGTH = 254

PHONE_LENGTH = 12


class CommunicationMethod(ProjectAttribute):
    """Предпочитаемый пользователем метод связи"""

    class Meta:
        verbose_name = "Метод связи"
        verbose_name_plural = "Методы связи"


class User(AbstractUser):
    """Класс описания пользователя."""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(
        "Электронная почта", max_length=EMAIL_LENGTH, unique=True
    )
    is_seller = models.BooleanField(
        "Продавец",
        default=False,
        help_text='Является ли пользователь продавцом',
    )
    personal_account_filled = models.BooleanField(
        'Заполнена информация в ЛК',
        default=False,
        help_text='Заполнил ли пользователь информацию о себе в ЛК',
    )
    first_name_ru = models.CharField(
        "Имя русское", max_length=settings.NAMES_LENGTH, blank=True
    )
    first_name_eng = models.CharField(
        "Имя английское", max_length=settings.NAMES_LENGTH, blank=True
    )
    last_name_ru = models.CharField(
        "Фамилия русская", max_length=settings.NAMES_LENGTH, blank=True
    )
    last_name_en = models.CharField(
        "Фамилия английская", max_length=settings.NAMES_LENGTH, blank=True
    )
    avatar = models.ImageField(
        "Аватар", upload_to="avatars/", default="avatars/default.png"
    )
    about_ru = models.TextField("О себе ru", default="")
    about_en = models.TextField("О себе eng", blank=True)
    style = models.ManyToManyField(
        Style, related_name="style_users", verbose_name="Стили", blank=True
    )
    materials = models.ManyToManyField(
        Material,
        related_name="_material_users",
        verbose_name="Материалы",
        blank=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name="Страна",
        blank=True,
        null=True,
    )
    address = models.CharField("Адрес", max_length=255, unique=True)
    communication_method = models.ForeignKey(
        CommunicationMethod,
        related_name='users',
        verbose_name='Предпочитаемый метод связи',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    project = models.IntegerField("Проект", default=1)
    created_at = models.DateTimeField("Создано", auto_now_add=True)
    edited_at = models.DateTimeField("Отредактировано", auto_now=True)

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self) -> str:
        return f"{self.username}"
