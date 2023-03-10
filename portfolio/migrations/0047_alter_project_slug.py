# Generated by Django 4.1.2 on 2022-10-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0046_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-d3cc7c85-8727-4544-a3e0-c85eadad6d41",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
