# Generated by Django 5.0.6 on 2024-06-24 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("albums", "0001_initial"),
        ("artists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="artist",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albums",
                to="artists.artist",
                verbose_name="artist",
            ),
        ),
    ]
