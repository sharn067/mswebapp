# Generated by Django 5.0.6 on 2024-07-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playlists", "0004_playlist_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist",
            name="description",
            field=models.TextField(blank=True, max_length=500, verbose_name="description"),
        ),
    ]
