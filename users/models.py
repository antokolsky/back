"""Модели связанные с пользователем"""

from django.contrib.auth.models import AbstractUser
from django.db import models

EMAIL_LENGTH = 254
NAMES_LENGTH = 100
PHONE_LENGTH = 12


class Country(models.Model):
    """Класс Стран"""

    name_ru = models.CharField(
        "Название Русское", max_length=NAMES_LENGTH, blank=False, unique=True
    )
    name_en = models.CharField(
        "Название Английское",
        max_length=NAMES_LENGTH,
        blank=False,
        unique=True,
    )
    iso = models.CharField(
        "ISO классификация страны", max_length=10, blank=True, unique=True
    )

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ("name_ru",)

    def __str__(self) -> str:
        return f"{self.name_ru}"


class City(models.Model):
    """Класс городов"""

    name_ru = models.CharField(
        "Название Русское", max_length=NAMES_LENGTH, blank=False
    )
    name_en = models.CharField(
        "Название Английское", max_length=NAMES_LENGTH, blank=False
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Город",
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("name_ru",)

    def __str__(self) -> str:
        return f"{self.country.name_ru} - {self.name_ru}"


class Style(models.Model):
    name_ru = models.CharField(
        "Русское название", max_length=NAMES_LENGTH, unique=True
    )
    name_en = models.CharField(
        "Английское название", max_length=NAMES_LENGTH, unique=True, blank=True
    )

    class Meta:
        verbose_name = "Стиль"
        verbose_name_plural = "Стили"

    def __str__(self) -> str:
        return f"{self.name_ru}"


class Material(models.Model):
    name_ru = models.CharField(
        "Русское название", max_length=NAMES_LENGTH, unique=True
    )
    name_en = models.CharField(
        "Английское название", max_length=NAMES_LENGTH, unique=True, blank=True
    )

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self) -> str:
        return f"{self.name_ru}"


class CommunicationMethod(models.Model):
    mobile_phone = models.CharField(
        "Номер мобильного", max_length=PHONE_LENGTH, unique=True, blank=True
    )
    telegram = models.CharField(
        "Ник телеграмм", max_length=255, unique=True, blank=True
    )
    whatsapp = models.CharField(
        "Номер WhatsApp", max_length=PHONE_LENGTH, unique=True, blank=True
    )

    class Meta:
        verbose_name = "Методы связи"
        verbose_name_plural = "Методы связи"

    def __str__(self) -> str:
        return f"{self.mobile_phone}"


class User(AbstractUser):
    """Класс описания пользователя"""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "is_seller")
    email = models.EmailField(
        "Электронная почта", max_length=EMAIL_LENGTH, unique=True
    )
    is_seller = models.BooleanField("Продавец", default=False)


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name_ru = models.CharField(
        "Имя русское", max_length=NAMES_LENGTH, blank=True
    )
    first_name_eng = models.CharField(
        "Имя английское", max_length=NAMES_LENGTH, blank=True
    )
    last_name_ru = models.CharField(
        "Фамилия русская", max_length=NAMES_LENGTH, blank=True
    )
    last_name_en = models.CharField(
        "Фамилия английская", max_length=NAMES_LENGTH, blank=True
    )
    avatar = models.ImageField(
        "Аватар", upload_to=f"avatars/", default="avatars/default.png"
    )
    about_ru = models.TextField("О себе ru", default="")
    about_en = models.TextField("О себе eng", blank=True)
    style = models.ManyToManyField(
        Style, related_name="users_info", verbose_name="Стили"
    )
    materials = models.ManyToManyField(
        Material, related_name="users_info", verbose_name="Стили"
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="users_info",
        verbose_name="Страна",
    )
    address = models.CharField("Адрес", max_length=255, unique=True)
    communication_method = models.OneToOneField(
        CommunicationMethod,
        on_delete=models.CASCADE,
        related_name="users_info",
        verbose_name="Методы связи",
    )
    projects = models.IntegerField("Проект")
    edited_at = models.DateTimeField("Отредактировано", auto_now=True)

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self) -> str:
        return f"{self.user.username}"
