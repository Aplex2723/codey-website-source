# Generated by Django 4.1.2 on 2022-10-18 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0045_alter_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="slug",
            field=models.SlugField(
                default="project-1bf40e48-23b2-40a0-bd82-2b780c4cfe51",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]