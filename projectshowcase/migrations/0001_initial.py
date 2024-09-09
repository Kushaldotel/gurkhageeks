# Generated by Django 5.0.7 on 2024-08-16 04:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="projectshowcase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "type_of_project",
                    models.CharField(
                        max_length=100, verbose_name="Type of Project eg.mobileapp, ML"
                    ),
                ),
                ("description_of_project", models.TextField()),
                ("Challenges_faced", models.TextField()),
                ("suggestion", models.TextField()),
                ("technology_used", models.CharField(max_length=200)),
                ("project_link", models.URLField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projectshowcase",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
