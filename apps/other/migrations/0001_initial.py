# Generated by Django 5.0.6 on 2024-06-17 12:39

import apps.core.services
import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, unique=True, verbose_name="name")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default/track.jpg",
                        upload_to=apps.core.services.get_path_upload_image_genre,
                        validators=[apps.core.services.validate_image_size],
                        verbose_name="image",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(
                        blank=True, default="", image_field="image", max_length=25, samples=None
                    ),
                ),
            ],
            options={
                "verbose_name": "Genre",
                "verbose_name_plural": "Genres",
                "ordering": ["-created_at", "-updated_at"],
            },
        ),
    ]