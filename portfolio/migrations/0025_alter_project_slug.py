# Generated by Django 4.1.2 on 2022-10-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0024_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-ecbc7d10-9d31-431d-8e18-056d49bbc2c7",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
