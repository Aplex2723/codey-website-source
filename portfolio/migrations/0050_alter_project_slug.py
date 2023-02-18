# Generated by Django 4.1.2 on 2022-10-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0049_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-17345f03-9805-4a08-9396-c08a2addfe4f",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]