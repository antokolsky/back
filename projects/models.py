# models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

User = get_user_model()


class Style(models.Model):
    """Модель для стилей."""
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru


class Material(models.Model):
    """Модель для материалов."""
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru


class Project(models.Model):
    """Модель работы автора"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_ru = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.URLField(max_length=200)
    other_photos = models.JSONField(default=list, blank=True)
    style = models.ManyToManyField(Style)
    material = models.ManyToManyField(Material)
    description_ru = models.CharField(max_length=1000)
    description_en = models.CharField(max_length=1000, null=True, blank=True)
    prepayment = models.FloatField(null=True, blank=True)
    cost_of_project = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(100000)])
    total_cost = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(User, related_name='projects', on_delete=models.SET_NULL, null=True)
    is_moderated = models.BooleanField(default=False)

    def __str__(self):
        return self.name_ru

    def save(self, *args, **kwargs):
        if self.prepayment and self.cost_of_project:
            self.total_cost = int(self.prepayment) + self.cost_of_project
        super().save(*args, **kwargs)
