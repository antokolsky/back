# Generated by Django 5.0.6 on 2024-06-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaticPages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название страницы"),
                ),
                (
                    "description",
                    models.CharField(max_length=200, verbose_name="Описание страницы"),
                ),
                (
                    "content",
                    models.TextField(
                        max_length=1000, verbose_name="Содержимое страницы"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="static_pages/default_avatar.png",
                        upload_to="static_pages/",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статичная страница",
                "verbose_name_plural": "Статичные страницы",
                "ordering": ["-id"],
            },
        ),
    ]
