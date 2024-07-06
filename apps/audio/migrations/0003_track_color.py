# Generated by Django 5.0.6 on 2024-07-06 16:53

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("audio", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="track",
            name="color",
            field=colorfield.fields.ColorField(
                blank=True, default="", image_field="image", max_length=25, samples=None
            ),
        ),
    ]
