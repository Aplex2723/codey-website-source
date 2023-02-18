# Generated by Django 4.1.2 on 2022-10-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0012_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-e858dc87-6e76-4a51-8d61-3055e8eb6d00",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]