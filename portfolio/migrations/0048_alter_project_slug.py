# Generated by Django 4.1.2 on 2022-10-18 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0047_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-06a648b3-4833-488c-9926-b075af4c9c51",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]