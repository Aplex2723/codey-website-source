# Generated by Django 4.1.2 on 2022-10-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0020_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-458388e4-833a-405d-9c31-4f3213922bdd",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
