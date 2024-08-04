# Generated by Django 5.0.7 on 2024-07-31 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="communication_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="users.communicationmethod",
                verbose_name="Предпочитаемый метод связи",
            ),
        ),
    ]
