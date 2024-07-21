# Generated by Django 5.0.6 on 2024-07-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_type_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type_profile",
            field=models.CharField(
                choices=[("user", "User"), ("artist", "Artist")],
                default="user",
                max_length=20,
                verbose_name="type profile",
            ),
        ),
    ]