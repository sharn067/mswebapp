# Generated by Django 5.0.6 on 2024-07-23 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("albums", "0003_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="album",
            options={
                "ordering": ["-updated_at", "-created_at"],
                "verbose_name": "album",
                "verbose_name_plural": "albums",
            },
        ),
    ]
