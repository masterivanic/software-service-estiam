# Generated by Django 5.0.4 on 2024-04-17 16:51
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("estiamauth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="is_confirmed",
            field=models.BooleanField(default=True),
        ),
    ]
