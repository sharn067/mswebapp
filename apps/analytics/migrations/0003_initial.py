# Generated by Django 5.0.6 on 2024-07-22 00:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("analytics", "0002_initial"),
        ("audio", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="playlistplayed",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="playlist_plays",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="similarity",
            name="track",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="similarities", to="audio.track"
            ),
        ),
        migrations.AddField(
            model_name="similarity",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="similarities", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="trackplayed",
            name="track",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="plays", to="audio.track"
            ),
        ),
        migrations.AddField(
            model_name="trackplayed",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="plays",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="playlistplayed",
            unique_together={("user", "playlist", "viewer_ip")},
        ),
        migrations.AlterUniqueTogether(
            name="similarity",
            unique_together={("user", "track")},
        ),
        migrations.AlterUniqueTogether(
            name="trackplayed",
            unique_together={("user", "track", "viewer_ip")},
        ),
    ]
