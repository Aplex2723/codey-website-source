# Generated by Django 4.1.2 on 2022-10-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HTMLModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clients", models.PositiveIntegerField(default=0)),
                ("projects", models.PositiveIntegerField(default=0)),
                ("support", models.PositiveIntegerField(default=0)),
                ("workers", models.PositiveIntegerField(default=0)),
                ("html_skills_percentage", models.PositiveIntegerField(default=0)),
                ("css_skills_percentage", models.PositiveIntegerField(default=0)),
                ("js_skills_percentage", models.PositiveIntegerField(default=0)),
                ("py_skills_percentage", models.PositiveIntegerField(default=0)),
                ("db_skills_percentage", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
