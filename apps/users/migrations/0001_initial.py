# Generated by Django 5.0.6 on 2024-06-24 10:00

import apps.core.services
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(db_index=True, max_length=255, unique=True, verbose_name="email address")),
                ("display_name", models.CharField(blank=True, max_length=100, verbose_name="display name")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female"), ("other", "Other")],
                        default="male",
                        max_length=20,
                        verbose_name="gender",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default/profile.jpg",
                        upload_to=apps.core.services.get_path_upload_image_user,
                        validators=[apps.core.services.validate_image_size],
                        verbose_name="image",
                    ),
                ),
                ("country", django_countries.fields.CountryField(default="UA", max_length=2, verbose_name="country")),
                (
                    "type_profile",
                    models.CharField(
                        choices=[("user", "User"), ("artist", "Artist")],
                        default="user",
                        max_length=20,
                        verbose_name="type profile",
                    ),
                ),
                ("is_premium", models.BooleanField(default=False, verbose_name="is premium")),
                ("is_spam_email", models.BooleanField(default=False, verbose_name="is spam email")),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff status")),
                ("is_active", models.BooleanField(default=True, verbose_name="active")),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                (
                    "followers",
                    models.ManyToManyField(blank=True, related_name="following", to=settings.AUTH_USER_MODEL),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "subscription_plan",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="users",
                        to="subscriptions.subscriptionplan",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
