# Generated by Django 5.0.6 on 2024-06-17 12:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("audio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="track",
            name="release_date",
            field=models.DateField(
                blank=True, default=django.utils.timezone.now, null=True, verbose_name="release date"
            ),
        ),
    ]
