# Generated by Django 4.2.11 on 2024-03-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainPageData",
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
                ("img_url", models.CharField(max_length=1280)),
                ("text", models.TextField(max_length=500)),
            ],
        ),
    ]
