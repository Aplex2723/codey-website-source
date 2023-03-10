# Generated by Django 4.1.2 on 2022-10-18 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0016_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-1913cc7f-285b-4894-8e90-0cdf8c7b6eb7",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
