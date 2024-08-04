from django.conf import settings
from django.db import models


class Country(models.Model):
    """Класс Стран"""

    name_ru = models.CharField(
        "Название Русское",
        max_length=settings.NAMES_LENGTH,
        blank=False,
        unique=True,
    )
    name_en = models.CharField(
        "Название Английское",
        max_length=settings.NAMES_LENGTH,
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
        "Название Русское", max_length=settings.NAMES_LENGTH, blank=False
    )
    name_en = models.CharField(
        "Название Английское", max_length=settings.NAMES_LENGTH, blank=False
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
