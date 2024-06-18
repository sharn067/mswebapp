# Generated by Django 5.0.6 on 2024-06-18 20:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("analytics", "0001_initial"),
        ("audio", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="similarity",
            name="track",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="similarities", to="audio.track"
            ),
        ),
    ]