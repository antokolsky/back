# Generated by Django 5.1.2 on 2024-10-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing", "0005_alter_projectimage_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SculptureOrder",
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
                    "sculpture_name",
                    models.CharField(
                        max_length=200, verbose_name="Название скульптуры"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                (
                    "phone",
                    models.CharField(blank=True, max_length=50, verbose_name="Телефон"),
                ),
                (
                    "create_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
            ],
            options={
                "verbose_name": "Заказ скульптуры",
                "verbose_name_plural": "Заказы скульптур",
                "ordering": ("create_date",),
            },
        ),
    ]
