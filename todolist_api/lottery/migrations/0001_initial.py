# Generated by Django 4.2.3 on 2023-09-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("title", models.CharField(max_length=200)),
                (
                    "rarity",
                    models.CharField(
                        choices=[
                            ("3", "General"),
                            ("4", "Rare"),
                            ("5", "Epic"),
                            ("6", "Legendary"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]