# Generated by Django 4.1.2 on 2022-10-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0021_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-cc1da21a-2fd3-4aad-8869-272a0386747f",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
