# Generated by Django 5.0.6 on 2024-08-10 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_postcomments_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomments',
            name='likes',
        ),
    ]
