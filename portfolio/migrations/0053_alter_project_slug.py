# Generated by Django 4.1.2 on 2022-10-23 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0052_alter_project_project_website_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-b84b2864-135b-4cbf-aeb0-99054152a3e6",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]