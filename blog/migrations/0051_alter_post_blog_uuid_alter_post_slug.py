# Generated by Django 4.1.2 on 2022-10-18 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0050_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="64aca7a2-c7d7-4a9f-8c79-9464f351adf9", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-64aca7a2-c7d7-4a9f-8c79-9464f351adf9",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
