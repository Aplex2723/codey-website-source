# Generated by Django 4.1.2 on 2022-10-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0005_alter_project_project_date_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-8bd23488-b23b-4748-addc-e40644977563",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
