# Generated by Django 4.1.2 on 2022-10-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0047_alter_post_blog_uuid_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="2d887713-4cf7-4e58-96de-b0f63770d493", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-2d887713-4cf7-4e58-96de-b0f63770d493",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
