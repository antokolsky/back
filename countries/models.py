from django.conf import settings
from django.db import models


class Country(models.Model):
    """Страны"""

    name_ru = models.CharField(
        "Название на русском",
        max_length=settings.NAMES_LENGTH,
        blank=False,
        unique=True,
    )
    name_eng = models.CharField(
        "Название на английском",
        max_length=settings.NAMES_LENGTH,
        blank=False,
        unique=True,
    )
    iso = models.CharField(
        "ISO классификация страны", max_length=10, blank=False, unique=True
    )

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ("name_ru",)

    def __str__(self):
        return self.name_ru


class City(models.Model):
    """Города"""

    name_ru = models.CharField(
        "Название на русском", max_length=settings.NAMES_LENGTH, blank=False
    )
    name_eng = models.CharField(
        "Название на английском", max_length=settings.NAMES_LENGTH, blank=False
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="cities",
        verbose_name="Страна",
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("name_ru",)

    def __str__(self):
        return self.name_ru
