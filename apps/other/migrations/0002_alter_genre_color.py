# Generated by Django 5.0.6 on 2024-07-09 20:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("other", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="color",
            field=colorfield.fields.ColorField(default="#202020", image_field=None, max_length=25, samples=None),
        ),
    ]