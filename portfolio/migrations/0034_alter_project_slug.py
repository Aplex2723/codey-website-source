# Generated by Django 4.1.2 on 2022-10-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0033_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-73401eee-1ca5-4fc4-b4b8-4237f985c943",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]