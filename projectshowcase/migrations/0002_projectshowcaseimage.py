# Generated by Django 5.0.7 on 2024-08-16 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectshowcase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectShowcaseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='projectshowcase')),
                ('project_showcase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projectshowcase.projectshowcase')),
            ],
        ),
    ]