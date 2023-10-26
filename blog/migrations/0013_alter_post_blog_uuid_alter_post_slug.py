# Generated by Django 4.1.2 on 2022-10-16 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="blog_uuid",
            field=models.UUIDField(
                default="b0b41007-7e8c-4b7a-b10d-c500743a9317", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default="blog-b0b41007-7e8c-4b7a-b10d-c500743a9317",
                unique=True,
                verbose_name="URL (sin espacios)",
            ),
        ),
    ]
