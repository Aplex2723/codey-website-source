# Generated by Django 4.1.5 on 2023-01-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0053_alter_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='project-8cbf3b84-18e9-41f3-8088-a2b1b31080d4', unique=True, verbose_name='URL (sin espacios)'),
        ),
    ]
